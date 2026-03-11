from proccesses_operator import ProccessesOperator
from logger import Logger



def start_extract_and_publish():
    
    logger = Logger.get_logger()
    try:
        operator = ProccessesOperator()
        operator.mtd_extraction()
        for publish in operator.kafka_publish(topic_name="RAW_METADATA"):
            logger.info(publish)
    except Exception as e:
        logger.error(e)
        raise



if __name__ == "__main__":
    start_extract_and_publish()