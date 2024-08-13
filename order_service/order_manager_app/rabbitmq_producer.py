import pika
import os

MQ_HOST = os.getenv('MQ_HOST', 'localhost')
MQ_URL = f'amqp://{MQ_HOST}:5672'
EXCHANGE = 'orders'
QUEUE = 'order.process'

class RabbitMQProducer:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=MQ_HOST))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='fanout')

    def publish(self, message):
        self.channel.basic_publish(exchange=EXCHANGE, routing_key='', body=message)
    
    def close(self):
        if self.connection:
            self.connection.close()

# Create a single instance of the producer to be used across the application
rabbitmq_producer = RabbitMQProducer()
