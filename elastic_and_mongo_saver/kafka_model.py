from confluent_kafka import Producer, Consumer
import json



class KafkaProdConsum:

    def __init__(self, prod_config =None, consum_config =None):
        if prod_config:
            self.kafka_producer = self.get_producer(prod_config)
        if consum_config:
            self.kafka_consumer = self.get_consumer(consum_config)
        else:
            raise Exception("No instance of the model was created because no configurations were received.")
    
    def get_producer(self, config):
        kafka_producer = Producer(config)
        return kafka_producer
    

    def get_consumer(self, config):
        kafka_consumer = Consumer(config)
        return kafka_consumer

    
    def production_to_kafka(self, topic_name: str, events_list: list[dict]):
        try:
            counter = 0
            for doc in events_list:
                event = json.dumps(doc).encode('utf-8')
                self.kafka_producer.produce(topic=topic_name, value=event, callback=self.delivery_report)
                counter += 1
                print(f"published Metadata-Events number {counter} to Kafka Topic named {topic_name}")
            self.kafka_producer.flush()
        except Exception as e:
            raise Exception(f"Kafka Producer Failed. \n{e}")


    def consum_from_kafka(self, topic_name: str):
        if self.kafka_consumer is None:
            self.kafka_consumer = self.get_consumer()
        self.kafka_consumer.subscribe([topic_name])
        print(f"Kafka-onsumer is running and subscribed to {topic_name} topic")
        try:
            counter = 0
            while True:
                counter += 1
                msg =self.kafka_consumer.poll(1.0)
                if msg is None:
                    print(f"\nconsumer retry: {counter}\n")
                    continue
                if msg.error():
                    print("Kafks Error:", msg.error())
                    continue
                value = msg.value().decode('utf-8')
                doc = json.loads(value)
                yield doc
        except Exception as e:
            raise Exception(f"Kafka consuming failed. \n{e}")
        
        
    @staticmethod
    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered {msg.value().decode('utf-8')}")
            print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")