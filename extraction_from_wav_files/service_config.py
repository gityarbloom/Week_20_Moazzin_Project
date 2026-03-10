from dotenv import load_dotenv
import os
load_dotenv()


class Configuration:
    def __init__(self):
        self.data_path = os.getenv("VOICE_DATA", "c:/Users/משתמש/Desktop/CodeStudy/Week_20/Moazzin_Project/podcasts/")
        kafka_uri = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.prod_config = {"bootstrap.servers" : kafka_uri}