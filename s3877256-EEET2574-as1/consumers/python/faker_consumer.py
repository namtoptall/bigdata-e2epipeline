from kafka import KafkaConsumer
import os, json

if __name__ == "__main__":
    print("Starting Faker Consumer")
    TOPIC_NAME = os.environ.get("Faker_topic_name", "faker")    
    kafka_broker_url = os.environ.get("KAFKA_BROKER_URL", "localhost:9092")
    cassandra_host = os.environ.get("CASSANDRA_HOST", "localhost")
    cassandra_keyspace = os.environ.get("CASSANDRA_KEYSPACE", "kafkapipeline")

    print("Setting up Kafka consumer at {}".format(kafka_broker_url))
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[kafka_broker_url])
    
    print('Waiting for msg...')
    for msg in consumer:
        msg = msg.value.decode('utf-8')
        jsonData=json.loads(msg)
        # add print for checking
        print(jsonData)
  
  
