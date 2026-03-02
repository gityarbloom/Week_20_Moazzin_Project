from confluent_kafka import Producer
import json


class KafkaPublisher:

    def __init__(self, kafka_config: dict):
        self.prod = Producer(kafka_config)

    @staticmethod
    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered to Topic names: '{msg.topic()}' in KAFKA")


    def send_to_kafka(self, topic_name: str, data: dict):
        try:
            value = json.dumps(data).encode("utf-8")
            self.prod.produce(topic=topic_name, value=value, callback=self.delivery_report)
            self.prod.poll(0)
            return "\nSuccesful sending to kafka\n"
        except Exception as e:
            raise Exception(str(e))

    def close(self):
        self.prod.flush()