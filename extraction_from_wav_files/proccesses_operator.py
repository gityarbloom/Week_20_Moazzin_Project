from extraction import MetadataExtraction
from publish import KafkaPublisher
from service_config import Configuration
import json


class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        
        
    def mtd_extraction(self):
        mtd_list = MetadataExtraction(self.data_path).metadata
        return mtd_list
    

    def convert_to_bin_list(self, mtd_list: list):
        bin_list = []
        for j in mtd_list:
            bin_list.append(json.dumps(j))
        return bin_list
    

    def kafka_publish(self, topic_name: str, mtd_list: list):
        producer = KafkaPublisher(self.prod_config)
        bin_list = self.convert_to_bin_list(mtd_list)

        counter = 0
        for m in bin_list:
            producer.send_mtd_to_kafka(topic=topic_name, data=m)
            print(f"published Metadata-Events number {counter} to Kafka Topic named {topic_name}")
            counter += 1
        producer.close()
        yield f"""finshed to publish {counter} Metadata-Events to Kafka Topic named {topic_name}"""