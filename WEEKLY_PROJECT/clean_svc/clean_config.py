from dotenv import load_dotenv
import os



load_dotenv()

class IngestionConfig:
    def __init__(self):
        self.kafka_boots_etc = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.producer_config = self.get_producer_config()
        self.consumer_config = self.get_consumer_config()

    def get_producer_config(self):
        producer_config = {"bootstrap.servers": self.kafka_boots_etc}
        return producer_config

    def get_consumer_config(self):
        consumer_config = {
            "bootstrap.servers": self.kafka_boots_etc,
            "group.id": "text-team",
            "session.timeout.ms": 6000,
            "auto.offset.reset": "earliest",
            "allow.auto.create.topics": False
        }
        return consumer_config