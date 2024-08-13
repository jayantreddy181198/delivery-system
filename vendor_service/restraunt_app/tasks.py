from celery import shared_task, chain
import pika
import os
import logging
import json
import requests
import time

PREFETCH_COUNT = int(os.getenv('PREFETCH_COUNT'))
MQ_HOST = os.getenv('MQ_HOST')
MQ_PORT = os.getenv('MQ_PORT')
MQ_URL = f'amqp://{MQ_HOST}:{MQ_PORT}/'
ORDER_UPDATE_URL = os.getenv('ORDER_UPDATE_URL')

@shared_task
def update_order_status(order_id, status):
    try:
        response = requests.put(
            f'{ORDER_UPDATE_URL}{order_id}',
            headers={'Content-Type': 'application/json'},
            json={"status": status}
        )
        logging.info(f"Order ID {order_id} status updated to '{status}'. Response: {response.status_code}")
    except Exception as e:
        logging.error(f"Error updating order status: {e}")

@shared_task
def start_rabbitmq_consumer():
    try:
        # Establish connection
        connection = pika.BlockingConnection(pika.URLParameters(MQ_URL))
        channel = connection.channel()

        # Declare the exchange
        channel.exchange_declare(exchange='orders', exchange_type='fanout', durable=False)

        # Ensure the queue exists or create one if it doesn't
        channel.queue_declare(queue='order.process', durable=True)
        channel.queue_bind(exchange='orders', queue='order.process')

        # Set the prefetch count to limit the number of unacknowledged messages
        channel.basic_qos(prefetch_count=PREFETCH_COUNT)

        # Define the callback function to handle messages
        def callback(ch, method, properties, body):
            try:
                # Decode and process the message
                body_str = body.decode('utf-8')
                message = json.loads(body_str)
                order_id = message.get('id', 1)
                
                # Process the order
                update_order_status(order_id, 'accepted')
                time.sleep(30)
                update_order_status(order_id, 'delivered')

                # Acknowledge the message after processing
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except json.JSONDecodeError:
                logging.error(f"Invalid JSON: {body}")
                # Optionally, you can reject the message and requeue
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            except Exception as e:
                logging.error(f"Error processing message: {e}")
                # Optionally, you can reject the message without requeuing
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        # Start consuming messages
        channel.basic_consume(queue='order.process', on_message_callback=callback, auto_ack=False)

        print('Waiting for messages...')
        channel.start_consuming()

    except Exception as ex:
        logging.error(f"Error in RabbitMQ consumer: {ex}")
