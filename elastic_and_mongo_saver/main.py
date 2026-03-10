from service_engine_model import ServiceEngineModel
import uuid
from logger import Logger



logger = Logger.get_logger()
logger.info("The muazin started")
logger.error("ooooopsss data invalid")


engine = ServiceEngineModel()

elastic_properties = {
    'id': {'type': 'keyword'},
    'File_Name': {'type': 'text'},
    'File_Path': {'type': 'text'},
    'MegaByte_Size': {'type': 'integer'},
    'Audio_Track_Length': {'type': 'integer'}
    }



def play():
    for doc in engine.kafka_consuming("RAW_METADATA"):
        print(f"\n{doc}\n")

        document = {"id": f"{uuid.uuid4()}MB_SIZE_FILE_{doc['MegaByte_Size']}", "MetaData": doc}
        saving_result = engine.elastic_saver(elastic_index="moazin_metadata", properties=elastic_properties, doc=document)
        print(f"\n{saving_result}\n")

        file_path = doc["File_Path"]
        id = document["id"]
        storage_result = engine.gridfs_saver(file_path=file_path, id=id)
        print(f"\n{storage_result}\n")



if __name__ == "__main__":
    play()