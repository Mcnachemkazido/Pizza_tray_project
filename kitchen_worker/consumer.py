from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
from confluent_kafka import Consumer
from mongo import mongo_coll
load_dotenv()



consumer_config = {
    "bootstrap.servers": os.getenv("PIZZA_HOST_PORT_KAFKA"),
    "group.id": "kitchen-team",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders-pizza"])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"☢️☢️☢️ {msg.error()}")
        continue
    data = msg.value().decode('utf-8')
    pizza = json.loads(data)
    query_filter = {'unique_id':pizza['unique_id']}
    update_operation = {'$set': {' status': 'DELIVERED'}}







