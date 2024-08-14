from celery import shared_task
import pika
import os
from .views import send_confirmation
import logging
import json

PREFETCH_COUNT = int(os.getenv('PREFETCH_COUNT', 20))
MQ_HOST = os.getenv('MQ_HOST', 'localhost')
MQ_PORT = os.getenv('MQ_PORT')
MQ_URL = f'amqp://{MQ_HOST}:{MQ_PORT}/'

@shared_task
def start_rabbitmq_consumer_msg():
    try:
        # Establish connection
        connection = pika.BlockingConnection(pika.URLParameters(MQ_URL))
        channel = connection.channel()

        # Declare the EXCHANGE
        channel.exchange_declare(exchange='orders', exchange_type='fanout', durable=False)

        # Ensure the queue exists or create one if it doesn't
        channel.queue_declare(queue='orders.confirmations', durable=True)
        channel.queue_bind(exchange='orders', queue='orders.confirmations')

        # Set the prefetch count to limit the number of unacknowledged messages
        channel.basic_qos(prefetch_count=PREFETCH_COUNT)

        # Define the callback function to handle messages
        def callback(ch, method, properties, body):
            try:
                # Decode and process the message
                body_str = body.decode('utf-8')
                send_confirmation(body_str)  # Adjust this if send_confirmation expects a string
                
                # Acknowledge the message after successful processing
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except json.JSONDecodeError:
                logging.error(f"Invalid JSON: {body}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            except Exception as e:
                logging.error(f"Error processing message: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        # Start consuming messages
        channel.basic_consume(queue='orders.confirmations', on_message_callback=callback, auto_ack=False)

        print('Waiting for messages...')
        channel.start_consuming()

    except Exception as ex:
        logging.error(f"Error in RabbitMQ consumer: {ex}")
