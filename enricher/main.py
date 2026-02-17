import json
from consumer import consumer

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
        print(info)


except KeyboardInterrupt:
    print("good by 👋👋👋")


finally:
    consumer.close()






