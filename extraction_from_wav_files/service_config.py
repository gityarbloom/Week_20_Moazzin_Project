from enc_and_decryption import decryp_base_64
from dotenv import load_dotenv
import os
load_dotenv()



high_danger = """
R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
ixSZWZ1Z2VlcyxJQ0MsQkRT
"""
low_danger = """
RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQY
Wxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==
"""



class Configuration:
    def __init__(self):
        self.data_path = os.getenv("VOICE_DATA", "c:/Users/משתמש/Desktop/CodeStudy/Week_20/Moazzin_Project/podcasts/")
        kafka_uri = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
        self.prod_config = {"bootstrap.servers" : kafka_uri}
        self.low_risk = decryp_base_64(low_danger)
        self.high_risk = decryp_base_64(high_danger)
        