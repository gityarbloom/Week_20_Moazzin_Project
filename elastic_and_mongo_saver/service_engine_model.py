from service_configs import ServiceConfigurations
from mongo_gridfs_model import GridFSStorage
from elastic_model import Elastic_MTD_Stor
from kafka_model import KafkaProdConsum



class ServiceEngineModel:

    def __init__(self):
        self.config = ServiceConfigurations()
        self.kafka_consumer = None  
        self.elastic = None  
        self.gridfs = None  


    def get_kafka_event(self, topic_name: str):
        if not self.kafka_consumer:
            self.kafka_consumer = KafkaProdConsum(consum_config=self.config.consumer_config)
        return self.kafka_consumer.consum_from_kafka(topic_name)


    def save_in_elastic(self, doc: dict, total: int, elastic_index: str =None, properties: str =None):
        if not self.elastic:
            if not(elastic_index and properties):
                raise Exception("No instance of the model was created because no configurations \n(elastic_index and map-properties) were received.")
            else:
                self.elastic = Elastic_MTD_Stor(self.config.elastic_uri, elastic_index, properties)
        saving_result = self.elastic.save_es_document(doc=doc, total=total)
        return saving_result


    def gridfs_saver(self, file_path: str, id: str):
        if not self.gridfs:
            self.gridfs = GridFSStorage(self.config.mongo_uri_config, self.config.mongo_db_name)
        with open(file_path, "rb") as f:
            bin_file = f.read()
        storage_result = self.gridfs.save_in_gridfs(bin_file=bin_file, id=id)
        return storage_result