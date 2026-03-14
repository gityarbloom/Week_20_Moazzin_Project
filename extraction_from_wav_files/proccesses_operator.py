from risk_level_analys_model import RiskLevelAnalysis
from extraction import MetadataExtraction
from service_config import Configuration
from publish import *
import json


class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        self.producer = KafkaPublisher(self.prod_config)
        self.risks_analyser = RiskLevelAnalysis(Configuration().low_risk, Configuration().high_risk)

        
    def mtd_extraction(self):
        mtd = MetadataExtraction(self.data_path).metadata
        metadata = self.analys_risks(mtd)
        return metadata
    

    def analys_risks(self, metadata):
        text = metadata["Extrcted_Text"]
        metadata["Percent_bds"] = self.risks_analyser.get_percent_bds(text=text)
        metadata["Is_bds"] = self.risks_analyser.is_it_bds(text=text)
        metadata["Level_threat_bds"] = self.risks_analyser.get_level_threat_bds(text=text)
        self.risks_analyser.restart_analyser()
        return metadata
    

    def kafka_publish(self, topic_name: str, metadata: dict):
        mtd = metadata
        counter = metadata['File_Number']
        bin_mtd = json.dumps(mtd).encode("utf-8")
        self.producer.send_mtd_to_kafka(topic=topic_name, data=bin_mtd, total=counter)
        yield f"published Metadata-Events number {counter} to Kafka Topic named {topic_name}"