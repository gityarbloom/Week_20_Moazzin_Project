from proccesses_operator import ProccessesOperator

operator = ProccessesOperator()
metadata = operator.mtd_extraction()
publish_to_kafka = operator.kafka_publish(topic_name="RAW_METADATA", metadata=metadata)