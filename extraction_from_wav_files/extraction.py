from stt import SpeachToText
from tinytag import TinyTag
import os



class MetadataExtraction:

    def __init__(self, data_path):
        self.metadata = self.extract_metadata(data_path)

    def extract_metadata(self, data_path: str):

        stt_extractor = SpeachToText()
        if data_path[-1] == "/":
            data_path = data_path[:-1]

        mtd_list = []
        file_counter = 0

        for file in os.listdir(data_path):
            file_counter += 1
            metadata_file = {}
            file_path = f"{data_path}/{file}"

            audio = TinyTag.get(filename=file_path)
            metadata_file["File_Name"] = file
            metadata_file["File_Path"] = file_path
            metadata_file["MegaByte_Size"] = audio.filesize / 1000000
            metadata_file["Audio_Track_Length"] = int(audio.duration)
            metadata_file["Extrction_Text"] = stt_extractor.wav_file_to_text(audio_path=file_path)


            print(f"Extract the Metadata of File Number {file_counter}: {metadata_file}")
            mtd_list.append(metadata_file)
        return mtd_list