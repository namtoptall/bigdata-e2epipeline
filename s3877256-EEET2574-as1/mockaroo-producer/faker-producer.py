import asyncio
import configparser
import os
import time
from collections import namedtuple
from kafka import KafkaProducer
from faker import Faker
import json


KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TOPIC_NAME = os.environ.get("TOPIC_NAME")
SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))

t1_mid = Faker()

def get_registered_user():
    return {
        "name": t1_mid.name(),
        "address": t1_mid.address(),
        "phone": t1_mid.phone_number,
        "job": t1_mid.job(),
        "email": t1_mid.email(),
        "company": t1_mid.company(),
        "country": t1_mid.country(),
        "city": t1_mid.city(),
        "text": t1_mid.text(),
        "state": t1_mid.state(),
    }
    
def run():
    iterator = 0 
    print("setting kafka at {}".format(KAFKA_BROKER_URL))
    producer = KafkaProducer(
        bootstrap_servers = [KAFKA_BROKER_URL],
        value_serializer = lambda x : json.dumps(x).encode('utf-8'),
    )
        
    while True:
        sendit = get_registered_user()
        print("Sending new faker data iteration - {}".format(iterator))
        producer.send(TOPIC_NAME, value=sendit)
        print("New faker data sent")
        time.sleep(SLEEP_TIME)
        print("Waking up!")
        iterator += 1
        
if __name__ == "__main__":
    run()
    