from mongo_loader_sending import MongoLoaderClient
from metadata_extractor import MetadataExtractor
from kafka_publisher import KafkaPublisher
from ocr_ngine import OCREngine
from ingestion_config import IngestionConfig
import os



pathsss = IngestionConfig()

folder_path = str(pathsss.folder_path)

mdb_loader_uri = str(pathsss.mongo_loader_uri)
mongo_loader_sending = MongoLoaderClient(mdb_loader_uri)

m_data_extractor = MetadataExtractor()

kafka_config = pathsss.kafka_config
kafka_producer = KafkaPublisher(kafka_config)

ocr_uri = str(pathsss.ocr_uri)
ocr_engine = OCREngine(ocr_uri)



def get_all_files_path(folder_path: str):
    all_files_path = []
    for f in os.listdir(folder_path):
        if f.endswith('.png'):
            file_path = f"{folder_path}/{f}"
            all_files_path.append(file_path)
    return all_files_path


def read_to_binary(file_path: str):
    with open(file_path, "rb") as f:
        return f.read()

def extract_text(image_path):
    raw_text = ocr_engine.get_extracted_text(image_path=image_path)
    return raw_text