from config import Configuration
from metadata_extraction import MetadataExtraction



config = Configuration()
data_path = config.publish_config
# "c:/Users/משתמש/Desktop/CodeStudy/Week_20/Moazzin_Project/podcasts/"

raw_metadata = MetadataExtraction(data_path=data_path)
metadata = raw_metadata.convert_to_jsons_list()

