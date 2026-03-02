from confluent_kafka import Consumer
import json
import time



class KafkaConsumer:

    def __init__(self, config: dict):
        self.consumer = self.get_consumer(config)


    def get_consumer(self, config: dict):
        for i in range(10):
            try:
                consum = Consumer(config)
                return consum
            except Exception as e:
                print(f"Kafka retry {i+1}/10...", e)
                if i == 9: raise Exception("Kafka failed")
                time.sleep(1)


    def listen_to_kafka(self, topic_name: str):
        self.consumer.subscribe([topic_name])
        print(f"✅ Kafka Consumer is listening to {topic_name} topic")
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print("❌ Error:", msg.error())
                    continue
                value = msg.value().decode('utf-8')
                dict_msg = json.loads(value)
                return dict_msg
        except KeyboardInterrupt:
            print("\n🔴 Enricher_Worker stopped")
        finally:
            self.consumer.close()