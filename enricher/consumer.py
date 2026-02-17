from dotenv import load_dotenv
from confluent_kafka import Consumer
import os
load_dotenv()


consumer_config = {
    "bootstrap.servers": os.getenv("PIZZA_HOST_PORT_KAFKA"),
    "group.id": "enricher-team",
    "auto.offset.reset": "earliest"
}


consumer = Consumer(consumer_config)

