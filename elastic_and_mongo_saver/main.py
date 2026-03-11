from service_engine_model import ServiceEngineModel
from logger import Logger
import uuid



def play():
    
    logger = Logger.get_logger()
    engine = ServiceEngineModel()
    elastic_properties = {
        'id': {'type': 'keyword'},
        'File_Name': {'type': 'text'},
        'File_Path': {'type': 'text'},
        'MegaByte_Size': {'type': 'integer'},
        'Audio_Track_Length': {'type': 'integer'}
        }

    try:
        for doc in engine.get_kafka_event("RAW_METADATA"):
            logger.info("Received Kafka document")
            document = {"id": f"{uuid.uuid4()}MB_SIZE_FILE_{doc['MegaByte_Size']}", "MetaData": doc}
            saving_result = engine.save_in_elastic(elastic_index="moazin_metadata", properties=elastic_properties, doc=document)
            logger.info(saving_result)
                
            file_path = doc["File_Path"]
            id = document["id"]
            storage_result = engine.gridfs_saver(file_path=file_path, id=id)
            logger.info(storage_result)
    except Exception as e:
        logger.error(e)
        raise


if __name__ == "__main__":
    play()