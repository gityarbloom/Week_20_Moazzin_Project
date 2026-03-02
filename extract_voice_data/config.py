from dotenv import load_dotenv
import os
load_dotenv()


class Configuration:
    def __init__(self):
        self.data_path = os.getenv("VOICE_DATA", "../podcasts/")
        self.publish_config = self.get_publish_config()

    def get_publish_config(self):
            pub_config = {'bootstrap.servers' : os.getenv("KAFKA_BOOTSTRAP_SERVERS")}
            return pub_config