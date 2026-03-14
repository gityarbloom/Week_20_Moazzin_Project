from proccesses_operator import *
from logger import Logger



def start_extract_and_publish():
    
    logger = Logger.get_logger()

    try:

        operator = ProccessesOperator()

        if type(operator.producer) == Exception:
            logger.error(operator.producer)

        for metadata in operator.mtd_extraction():
            print()
            logger.info(f"Extract the Metadata of File Number {metadata['File_Number']}: {metadata}")
            
            for publish in operator.kafka_publish(topic_name="RAW_METADATA", metadata=metadata):
                print()
                logger.info(publish)

        operator.producer.close()

    except Exception as e:
        
        logger.error(e)
        raise



if __name__ == "__main__":
    start_extract_and_publish()