from extraction import MetadataExtraction
from publish import KafkaPublisher
from service_config import Configuration
import json


class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        
        
    def mtd_extraction(self):
        self.mtd_list = MetadataExtraction(self.data_path).metadata
        return self.mtd_list
    

    def convert_to_bin_list(self):
        bin_list = []
        for j in self.mtd_list:
            bin_list.append(json.dumps(j))
        return bin_list
    

    def kafka_publish(self, topic_name: str):
        producer = KafkaPublisher(self.prod_config)
        bin_list = self.convert_to_bin_list()

        counter = 0
        for m in bin_list:
            producer.send_mtd_to_kafka(topic=topic_name, data=m)
            print(f"published Metadata-Events number {counter} to Kafka Topic named {topic_name}")
            counter += 1
        producer.close()
        print(f"""finshed to publish {counter} Metadata-Events to Kafka Topic named {topic_name}""")