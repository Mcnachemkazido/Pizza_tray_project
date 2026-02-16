from fastapi import APIRouter ,HTTPException, File, UploadFile
import json

from schemes import Item
from mongo import mongo_coll
from producer import producer ,delivery_report
from conn_redis import conn_redis




route = APIRouter()

@route.post("/upload_file")
def create_upload_files(upload_file: UploadFile = File(...)):
    try:
        json_data = json.load(upload_file.file)
        for item in json_data:
            extended_item = Item(**item)
            mongo_coll.insert_one(extended_item.model_dump())
            producer.produce(
                topic= "orders-pizza",
                value=(extended_item.model_dump_json()).encode('utf-8'),
                callback=delivery_report
            )
            producer.flush()
        return {True :"Page loaded successfully. Sent to kafka and to mongodb"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail=e)



@route.get("/order/{order_id}")
def get_order_by_id(order_id):
    try:
        if conn_redis.get(order_id) is not None:
            result = json.loads(conn_redis.get(order_id))
            source = "redis_cache"
            ttl = conn_redis.ttl(order_id)
        else:
            result = mongo_coll.find({"order_id": order_id},{"_id":0}).to_list()
            conn_redis.setex(order_id,3600,json.dumps(result))
            source = "mongodb"
            ttl = conn_redis.ttl(order_id)
        return {"source":source,"ttl":ttl,"result":result}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail=e)

