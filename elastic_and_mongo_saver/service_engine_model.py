from service_configs import ServiceConfigurations
from mongo_gridfs_model import GridFSStorage
from elastic_model import Elastic_MTD_Stor
from kafka_model import KafkaProdConsum


class ServiceEngineModel:


    def kafka_consuming(self, topic_name: str):
        consum_config = ServiceConfigurations().consumer_config
        kafka = KafkaProdConsum(consum_config=consum_config)
        event = kafka.consum_from_kafka(topic_name)
        return event


    def elastic_saver(self, elastic_index: str, properties: str, doc: dict):
        try:
            elastic_uri = ServiceConfigurations().elstic_uri
            elastic = Elastic_MTD_Stor(elastic_uri, elastic_index, properties)
            saving_result = elastic.save_es_document(doc=doc)
            return saving_result
        except Exception as e:
            print("elastic saving failed", e)        

    def gridfs_saver(self, file_path: str, id: str):
        mongo_uri = ServiceConfigurations().mongo_uri_config
        mongo_db_name = ServiceConfigurations().mongo_db_name
        gridfs = GridFSStorage(mongo_uri=mongo_uri, mongo_db_name=mongo_db_name)
        with open(file_path, "rb") as f:
            bin_file = f.read()
        storage_result = gridfs.save_in_gridfs(bin_file=bin_file, id=id)
        return storage_result