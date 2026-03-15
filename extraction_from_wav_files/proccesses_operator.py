from extraction import MetadataExtraction
from service_config import Configuration
from publish import *
import json


class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        self.producer = KafkaPublisher(self.prod_config)
        self.low_risk = Configuration().low_risk
        self.high_risk = Configuration().high_risk

        
    def mtd_extraction(self):
        mtd = MetadataExtraction(self.data_path, self.low_risk, self.high_risk).metadata
        return mtd
    

    def kafka_publish(self, topic_name: str, metadata: dict):
        mtd = metadata
        counter = metadata['File_Number']
        bin_mtd = json.dumps(mtd).encode("utf-8")
        self.producer.send_mtd_to_kafka(topic=topic_name, data=bin_mtd, total=counter)
        yield f"published Metadata-Event number {counter} to Kafka Topic named {topic_name}"