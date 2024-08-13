import json
import pika
import os

# Load environment variables
MQ_HOST = os.getenv('MQ_HOST', 'localhost')
MQ_PORT = os.getenv('MQ_PORT')
MQ_URL = f'amqp://{MQ_HOST}:{MQ_PORT}/'
EXCHANGE = os.getenv('EXCHANGE', 'orders')
ROUTING_KEY = os.getenv('ROUTING_KEY', '')

class RabbitmqProducer:
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.URLParameters(MQ_URL))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout', durable=False)

    def publish(self, method, body):
        print('Inside RabbitmqProducer: Sending to RabbitMQ:')
        properties = pika.BasicProperties(content_type='application/json')
        self.channel.basic_publish(exchange=EXCHANGE, routing_key=ROUTING_KEY, body=body, properties=properties)