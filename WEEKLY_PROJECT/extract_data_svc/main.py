from ingestion_orchestrator import *
import time

time.sleep(15)

images_path_list = get_all_files_path(folder_path)

send_count = 0

for i in range(len(images_path_list)):
    image_id = images_path_list[i]
    bin_txt = read_to_binary(image_id)
    send_count += 1
    mongo_loader_sending.send_to_mongo_loader(image_id, bin_txt, send_count)

    raw_txt = extract_text(image_id)
    metadata = m_data_extractor.extract_metadata(image_id)
    data = {"image_id": image_id, "raw_txt": raw_txt, "metadata": metadata}    
    send_to_kafka = kafka_producer.send_to_kafka("RAW", data)
    print(send_to_kafka)

kafka_producer.close()

print("\n'extract_data_service' operation terminated. \nThe server has closed because it has completed all tasks.")