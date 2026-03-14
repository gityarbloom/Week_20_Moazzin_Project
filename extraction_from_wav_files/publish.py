from confluent_kafka import Producer
import time



class KafkaPublisher:

    def __init__(self, prod_config):
        self.producer = self.get_kafka_publisher(prod_config)


    def get_kafka_publisher(self, publisher_config):
        for i in range(10):
            try:
                producer = Producer(publisher_config)
                return producer
            except Exception as e:
                if i == 9: 
                    return Exception(f"Kafka failed, \nDetails: {e}")
                time.sleep(0.5)
            print(f"Kafka retry {i+1} /10...")   


    def send_mtd_to_kafka(self, topic: str, data: bytes, total: int):
            try:
                self.producer.produce(topic=topic, value=data) #, callback=self.delivery_report)
                self.producer.poll(0)
                return f"Kafka publish number {total} was successfuly finished"
            except Exception as e:
                return Exception(f"Kafka Publish number {total} Failed. \nnDetails: {e}")

    # @staticmethod
    # def delivery_report(err, msg):
    #     if err:
    #         print()
    #         print(f"❌ Delivery failed: {err}")
    #     else:
    #         print()
    #         print(f"✅ Delivered to KAFKA-Topic named: '{msg.topic()}'")


    def close(self):
        time.sleep(10)
        self.producer.flush()
        self.producer = None