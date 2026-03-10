from proccesses_operator import ProccessesOperator
from logger import Logger



logger = Logger.get_logger()
logger.info("The muazin started")
logger.error("ooooopsss data invalid")


def start_extract_and_publish():
    operator = ProccessesOperator()
    metadata = operator.mtd_extraction()
    operator.kafka_publish(topic_name="RAW_METADATA")


if __name__ == "__main__":
    start_extract_and_publish()