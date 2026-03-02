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
        
    def send_mtd_to_kafka(self, events_list):
        for e in events_list:
            self.publisher.produce("METADATA", )