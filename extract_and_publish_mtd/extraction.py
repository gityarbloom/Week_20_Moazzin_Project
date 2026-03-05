from tinytag import TinyTag
import os



class MetadataExtraction:

    def __init__(self, data_path):
        self.metadata = self.extract_metadata(data_path)

    def extract_metadata(self, data_path: str):
        mtd_list = []
        file_counter = 0

        for file in os.listdir(data_path):
            mtd = {}
            file_path = f"{data_path}{file}"
            file_counter += 1
            metadata_file = {}
            audio = TinyTag.get(filename=file_path)
            metadata_file["File Name"] = file
            metadata_file["File Path"] = file_path
            metadata_file["MegaByte Size"] = audio.filesize / 1000000
            metadata_file["Playback Duration on Seconds"] = int(audio.duration)
            mtd[f"Metadata of File Number {file_counter}"] = metadata_file
            mtd_list.append(metadata_file)
        return mtd_list