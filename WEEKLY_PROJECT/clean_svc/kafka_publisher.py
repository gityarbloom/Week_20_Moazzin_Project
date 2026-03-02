from confluent_kafka import Producer
import json
import time


class KafkaPublisher:

    def __init__(self, config: dict):
        self.prod = self.get_producer(config)


    def get_producer(self, config: dict):
        for i in range(10):
            try:
                prod = Producer(config)
                return prod
            except Exception as e:
                print(f"Kafka retry {i+1}/10...", e)
                if i == 9: raise Exception("Kafka failed")
                time.sleep(1)


    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered to Topic names: '{msg.topic()}' in KAFKA")


    def send_to_kafka(self, topic_name: str, data: bytes):
        try:
            self.prod.produce(topic=topic_name, value=value, callback=self.delivery_report)
            self.prod.poll(0)
            return "\nSuccesful sending to kafka\n"
        except Exception as e:
            raise Exception(str(e))

    def close(self):
        self.prod.flush()