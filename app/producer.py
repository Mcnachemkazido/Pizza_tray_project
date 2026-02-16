from dotenv import load_dotenv
import os
load_dotenv()
from confluent_kafka import Producer


producer_config = {
    "bootstrap.servers": os.getenv("PIZZA_HOST_PORT_KAFKA")
}

producer = Producer(producer_config)


def delivery_report(err, msg):
    if err:
        print(f"⛔⛔⛔ Delivery failed: {err}")
    else:
        print(f"👍👍👍 Delivered {msg.value().decode('utf-8')}")
        print(f"👌👌👌 Delivered to {msg.topic()}, at offset {msg.offset()}")
