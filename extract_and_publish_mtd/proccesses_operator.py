from extraction import MetadataExtraction
from publish import KafkaPublisher
from config import Configuration
import json



class ProccessesOperator:
    def __init__(self):
        self.prod_config = Configuration().prod_config
        self.data_path = Configuration().data_path
        
        
    def mtd_extraction(self):
        mtd_list = MetadataExtraction(self.data_path).metadata
        self.mtd_jsons_list = self.convert_to_jsons_list(mtd_list=mtd_list)
        return self.mtd_jsons_list
    

    def convert_to_jsons_list(self, mtd_list):
        jsons_list = []
        for j in mtd_list:
            jsons_list.append(json.dumps(j))
        return jsons_list
    

    def kafka_publish(self, topic_name):
        producer = KafkaPublisher(self.prod_config)

        print(f"""Now starting to publish {len(self.json_mtd_list)} Metadata-Events to Kafka Topic named {topic_name}""")
        counter = 0
        for m in self.json_mtd_list:
            producer.send_mtd_to_kafka(topic=topic_name, data=m)
            counter += 1

        producer.close()
        print(f"""Now finshed to publish {counter} Metadata-Events to Kafka Topic named {topic_name}""")