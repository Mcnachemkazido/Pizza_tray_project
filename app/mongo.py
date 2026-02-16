from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
USER=os.getenv("PIZZA_MONGO_USER")
PASS=os.getenv("PIZZA_MONGO_PASS")
HOST=os.getenv("PIZZA_MONGO_HOST")
PORT=os.getenv("PIZZA_MONGO_PORT")
URI = f"mongodb://{USER}:{PASS}@{HOST}:{PORT}"

def get_mongo_coll(uri):
    client = MongoClient(uri)
    db = client['store']
    coll = db['pizza']
    return coll



mongo_coll = get_mongo_coll(URI)


