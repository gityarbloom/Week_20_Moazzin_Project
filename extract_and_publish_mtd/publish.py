from confluent_kafka import Producer



class KafkaPublisher:

    def __init__(self, publisher_config):
        self.publisher = self.get_kafka_publisher(publisher_config)


    def get_kafka_publisher(self, publisher_config):
        try:
            producer = Producer(config=publisher_config)
            return producer
        except Exception as e:
            raise Exception(f"Kafka Connect Failed. \nDetails: {e}")
        

    def send_mtd_to_kafka(self, topic: str, data: str):
            try:
                value = data.encode("utf-8")
                self.publisher.produce(topic=topic, value=value, callback=self.delivery_report)
                self.publisher.poll(0)
            except Exception as e:
                raise Exception(f"Kafka Publish Failed: {e}")

    @staticmethod
    def delivery_report(err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered to Topic names: '{msg.topic()}' in KAFKA")


    def close(self):
        self.publisher.flush()