from fastapi import APIRouter ,HTTPException, File, UploadFile
import json

from schemes import Item
from mongo import mongo_coll
from producer import producer ,delivery_report


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


