from dotenv import load_dotenv
import os


class ServiceConfigurations:

    def __init__(self):
        load_dotenv()
        self.data_path = os.getenv("VOICE_DATA", "c:/Users/משתמש/Desktop/CodeStudy/Week_20/Moazzin_Project/podcasts/")
        self.elstic_uri = os.getenv("ES_URI")
        self.kafka_boots_etc = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:29092")
        self.producer_config = {"bootstrap.servers": self.kafka_boots_etc}
        self.consumer_config = {
            "bootstrap.servers": self.kafka_boots_etc,
            "group.id": "metadata_group",
            "session.timeout.ms": 6000,
            "auto.offset.reset": "earliest",
            "allow.auto.create.topics": False
        }
        self.mongo_uri_config = os.getenv("MONGO_URI", "localhost:27017")
        self.mongo_db_name = "moazin-db"