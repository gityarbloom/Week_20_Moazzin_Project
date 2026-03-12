from extraction import MetadataExtraction
from publish import KafkaPublisher
from service_config import Configuration
import json


class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        self.producer = KafkaPublisher(self.prod_config)
        
        
    def mtd_extraction(self):
        mtd = MetadataExtraction(self.data_path).metadata
        return mtd
    

    def convert_to_bin(self, mtd: dict):
        bin_mtd = json.dumps(mtd).encode("utf-8")
        return bin_mtd
    

    def kafka_publish(self, topic_name: str, metadata: tuple):
        mtd = metadata[0]
        counter = metadata[1]
        bin_mtd = self.convert_to_bin(mtd)

        self.producer.send_mtd_to_kafka(topic=topic_name, data=bin_mtd)
        yield f"published Metadata-Events number {counter} to Kafka Topic named {topic_name}"