import json
from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    "bootstrap.servers": "agile-kafka:9092",
    "group.id": "notification-service-1",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": True,
})

def start_consumer():
    print("CONSUMER LOOP STARTED", flush=True)

    consumer.subscribe(["issue.created"])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART:
                    continue
                print("Kafka error:", msg.error(), flush=True)
                continue

            data = json.loads(msg.value().decode("utf-8"))
            print("Received event:", data, flush=True)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
