from dotenv import load_dotenv
import os
import json
from confluent_kafka import Consumer
from mongo import mongo_coll
import utils
load_dotenv()



consumer_config = {
    "bootstrap.servers": os.getenv("PIZZA_HOST_PORT_KAFKA"),
    "group.id": "text-team",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders-pizza"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"☢️☢️☢️ {msg.error()}")
            continue
        data = msg.value().decode('utf-8')
        pizza = json.loads(data)

        data_searching = utils.search_in_text(pizza)
        data_clearing = utils.clearing_the_data(data_searching)
        utils.clearing_the_data(pizza)
        query_filter = {'unique_id': pizza['unique_id']}
        update_operation = {'$set': {"cleaned_protocol":data_clearing['cleaned_protocol'],
                                     "allergies_flagged":data_clearing['allergies_flagged']}}
        mongo_coll.update_one(query_filter, update_operation)
        print(f"😃😃😃😃😃I updated two additional fields in mongodb in user\n{pizza['unique_id']}")

except KeyboardInterrupt:
    print("good by 👋👋👋")


finally:
    consumer.close()







