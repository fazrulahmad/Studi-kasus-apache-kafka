import time
import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

sensor_ids = ['S1', 'S2', 'S3']

while True:
    for sensor_id in sensor_ids:
        suhu = random.randint(60, 100)
        data = {'sensor_id': sensor_id, 'suhu': suhu}
        
        producer.send('sensor-suhu', value=data)
        print(f"Data dikirim: {data}")

    time.sleep(1)
