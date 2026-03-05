from dotenv import load_dotenv
import os
load_dotenv()


class Configuration:
    def __init__(self):
        self.data_path = os.getenv("VOICE_DATA", "../podcasts/")
        self.prod_config = {'bootstrap.servers' : os.getenv("KAFKA_BOOTSTRAP_SERVERS")}