from clean_config import IngestionConfig
from kafka_publisher import KafkaPublisher
from kafka_consumer import KafkaConsumer
from text_cleaner import TextCleaner



class CleanOrchestrator:

    def __init__(self):
        self.config = IngestionConfig()
        self.prod_config = self.config.producer_config
        self.consum_config = self.config.consumer_config
        self.producer = KafkaPublisher(self.prod_config)
        self.consumer = KafkaConsumer(self.consum_config)
        self.text_cleaner = TextCleaner()



    def constructor(self, event_num):

        kafka_event = self.consumer.listen_to_kafka("RAW")
        text = kafka_event["raw_txt"]
        cllean_text = str(self.text_cleaner.clean_text(text))
        data = cllean_text.encode("utf-8")
        self.producer.send_to_kafka("CLEAN", data=data)
        return f"'CLEAN' event was successfuly delivered to 'CLEAN' kafka topic ✌️. \nEvent num: {event_num}"