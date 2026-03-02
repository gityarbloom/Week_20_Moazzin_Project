from dotenv import load_dotenv
from tinytag import TinyTag
import json
import os
load_dotenv()

class MetadataExtraction:

    def __init__(self, data_path):
        self.metadata = self.extract_metadata(data_path)

    def extract_metadata(self, data_path):
        mtd_list = []
        file_counter = 0
        for file in os.listdir(data_path):
            mtd = {}
            if file.endswith(".wav"):
                file_path = f"{data_path}{file}"
                file_counter += 1
                metadata_file = {}
                audio = TinyTag.get(filename=file_path)
                metadata_file["File Name"] = file
                metadata_file["MegaBytes Size"] = audio.filesize / 1000000
                metadata_file["Playback Duration on Seconds"] = int(audio.duration)
                mtd[f"Metadata of File Number {file_counter}"] = metadata_file
                mtd.append(metadata_file)
        return mtd
    
    def convert_to_jsons_list(self):
        jsons_list = []
        for j in self.metadata:
            jsons_list.append(json.dumps(j))
        return jsons_list
    
reger = MetadataExtraction()