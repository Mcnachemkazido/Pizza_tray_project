import json
from consumer import consumer
from mongo import mongo_coll
from utils import update_new_fields
from conn_redis import conn_redis

consumer.subscribe(["cleaned-instructions"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"☢️☢️☢️ {msg.error()}")
            continue
        data = msg.value().decode('utf-8')
        info = json.loads(data)
        info_type = info['pizza_type']
        order_id = info['order_id']

        if conn_redis.get(info_type) is not None:
            update_info = json.loads(conn_redis.get(info_type))
            print(f"cache hit for info type {info_type}")
            print(f"ttl:{conn_redis.ttl(info_type)}")
        else:
            update_info = update_new_fields(info)
            conn_redis.setex(info_type, 5, json.dumps(update_info))
            print(f"cache miss for info type {info_type}")
            print(info_type)

        filter = {'order_id':order_id}
        new_values = {"$set":{'is_allergic':update_info['is_allergic'],
                    'is_kosher':update_info['is_kosher'],
                    'is_meat':update_info['is_meat'], 'is_dairy':update_info['is_dairy'],
                    'is_vegan':update_info['is_vegan'], 'status':update_info['status'],
                     'special_instructions':update_info['clean_special_instructions']}}


        mongo_coll.update_one(filter,new_values)
        print(f"😄😁😆😅 I updated mongodb with new fields 'order_id':{order_id}")


except KeyboardInterrupt:
    print("good by 👋👋👋")


finally:
    consumer.close()






