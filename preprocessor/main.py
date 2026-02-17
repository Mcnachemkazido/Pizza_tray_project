import json
from consumer import consumer
from producer import producer ,delivery_report
from utils import clearing_the_data, pulling_out_pizza_prep

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

        pizza_prep = pulling_out_pizza_prep(pizza['pizza_type'])
        clean_pizza_prep = clearing_the_data(pizza_prep)
        clean_special_instructions = clearing_the_data(pizza['special_instructions'])

        msg_send = {"order_id": pizza['order_id'], "pizza_type": pizza['pizza_type'],
                    "clean_special_instructions": clean_special_instructions,
                    "clean_pizza_prep": clean_pizza_prep}


        producer.produce(
            topic="cleaned-instructions",
            value=json.dumps(msg_send).encode('utf-8'),
            callback=delivery_report
        )
        producer.flush()


except KeyboardInterrupt:
    print("good by 👋👋👋")


finally:
    consumer.close()






