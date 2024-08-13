import pika
import json 
# RabbitMQ connection parameters
MQ_HOST = 'localhost'
MQ_URL = f'amqp://{MQ_HOST}:5672/'
EXCHANGE = 'orders'
ROUTING_KEY = ''  # Not used for fanout exchange
data = '{"id": 12345, "amount": 99.99, "recepient_email": "example@example.com"}'
MESSAGE = 'Hello, this is a test message for order confirmation!'

def publish_message():
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(MQ_URL))
    channel = connection.channel()

    # Declare the exchange
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout', durable=False)

    message_body = {
        "id": 12345,
        "amount": 99.99,
        "recepient_email": "jayantreddybodkurwar@gmail.com"
    }

    # Publish the message to the exchange
    channel.basic_publish(exchange=EXCHANGE, routing_key=ROUTING_KEY, body=json.dumps(message_body))
    
    print(f"Sent: {message_body}")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    publish_message()
