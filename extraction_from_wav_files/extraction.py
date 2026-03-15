from risk_level_analys_model import RiskLevelAnalysis
from stt import SpeachToText
from tinytag import TinyTag
import os



class MetadataExtraction:

    def __init__(self, data_path, low, high):
        self.risks_analyser = RiskLevelAnalysis(low, high)
        self.metadata = self.extract_metadata(data_path)


    def extract_metadata(self, data_path: str):
        
        stt_extractor = SpeachToText()
        if data_path[-1] == "/":
            data_path = data_path[:-1]

        file_counter = 0
        for file in os.listdir(data_path):
            file_counter += 1
            metadata_file = {}
            file_path = f"{data_path}/{file}"

            audio = TinyTag.get(filename=file_path)
            metadata_file["File_Name"] = file
            metadata_file["File_Number"] = file_counter
            metadata_file["File_Path"] = file_path
            metadata_file["MegaByte_Size"] = audio.filesize / 1000000
            metadata_file["Audio_Track_Length"] = int(audio.duration)
            metadata_file["Extrcted_Text"] = stt_extractor.wav_file_to_text(audio_path=file_path)

            text = metadata_file["Extrcted_Text"]
            metadata_file["Percent_bds"] = self.risks_analyser.get_percent_bds(text=text)
            metadata_file["Is_bds"] = self.risks_analyser.is_it_bds(text=text)
            metadata_file["Level_threat_bds"] = self.risks_analyser.get_level_threat_bds(text=text)
            # self.risks_analyser.restart_analyser()

            yield metadata_file