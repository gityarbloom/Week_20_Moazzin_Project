from confluent_kafka import Producer
import time



class KafkaPublisher:

    def __init__(self, prod_config):
        self.producer = self.get_kafka_publisher(prod_config)

    def get_kafka_publisher(self, publisher_config):
        for i in range(10):
            try:
                producer = Producer(publisher_config)
                print(f"Kafka retry {i+1}/10...")
                return producer
            except Exception as e:
                if i == 9: raise Exception(f"Kafka failed, \nDeatails: {e}")
                time.sleep(1)
            print(f"Kafka retry {i+1}/10...")   

    def send_mtd_to_kafka(self, topic: str, data: str):
            try:
                value = data.encode("utf-8")
                self.producer.produce(topic=topic, value=value, callback=self.delivery_report)
                self.producer.poll(0)
            except Exception as e:
                raise Exception(f"Kafka Publish Failed: {e}")

    @staticmethod
    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered to Topic names: '{msg.topic()}' in KAFKA")


    def close(self):
        time.sleep(10)
        self.producer.flush()