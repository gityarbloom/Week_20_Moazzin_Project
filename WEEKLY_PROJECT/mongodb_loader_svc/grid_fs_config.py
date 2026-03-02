from dotenv import load_dotenv
import os


load_dotenv()


class GridFSConfig:
    def __init__(self):
        self.mongo_uri =  os.getenv("MONGO_URI")
        self.mongo_db_name = os.getenv("MONGO_DATABASE_NAME")
        self.mongo_coll_name = os.getenv("MONGO_COLLECTION_NAME")