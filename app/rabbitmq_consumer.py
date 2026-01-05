import pika
import json
import threading
from app.notification_handler import process_notification_event
from app.database import SessionLocal
from app.config import settings

def callback(ch, method, properties, body):
    event_data = json.loads(body)
    db = SessionLocal()
    
    try:
        process_notification_event(event_data, db)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        
    except Exception as e:

        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        
    finally:
        db.close()

def start_rabbitmq_consumer():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(settings.RABBITMQ_URL)
    )
    channel = connection.channel()
    channel.queue_declare(queue='notifications', durable=True)
    channel.basic_consume(
        queue='notifications',
        on_message_callback=callback,
        auto_ack=False
    )
    channel.start_consuming()

def start_consumer_thread():
    consumer_thread = threading.Thread(target=start_rabbitmq_consumer, daemon=True)
    consumer_thread.start()