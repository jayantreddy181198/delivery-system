from celery import shared_task
from .rabbitmq_producer import rabbitmq_producer

@shared_task
def publish_order_message(order_data):
    try:
        # Serialize order_data to string format (e.g., JSON)
        message = json.dumps(order_data)
        rabbitmq_producer.publish(message)
        return True
    except Exception as e:
        # Handle exceptions and logging
        return False
