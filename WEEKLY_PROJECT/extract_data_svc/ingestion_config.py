from dotenv import load_dotenv
import os



load_dotenv()

class IngestionConfig:
    def __init__(self):
        self.ocr_uri = self.get_ocr_uri()
        self.folder_path = self.get_folder_path()
        self.kafka_config = self.get_producer_config()
        self.mongo_loader_uri = self.get_mongo_loader_uri()

    @staticmethod
    def get_ocr_uri():
        ocr_uri = os.getenv("OCR_URI")
        return ocr_uri
    
    @staticmethod
    def get_folder_path():
        folder_path = os.getenv("FOLDER_PATH")
        return folder_path
    
    @staticmethod
    def get_producer_config():
        kafka_boots_etc = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        kafka_config = {"bootstrap.servers": kafka_boots_etc}
        return kafka_config
    
    @staticmethod
    def get_mongo_loader_uri():
        mongo_loader_uri = os.getenv("MONGO_LOADER_URI")
        return mongo_loader_uri