from dotenv import load_dotenv
import os
load_dotenv()
import redis

REDIS_HOST=os.getenv("PIZZA_REDIS_HOST")
REDIS_PORT=int(os.getenv("PIZZA_REDIS_PORT"))

conn_redis = redis.Redis(host= REDIS_HOST,port=REDIS_PORT,decode_responses=True)



try:
    conn_redis.ping()
    print("👌👌redis is run")
except redis.exceptions.ConnectionError:
    print("⚠️⚠️ no conn")




