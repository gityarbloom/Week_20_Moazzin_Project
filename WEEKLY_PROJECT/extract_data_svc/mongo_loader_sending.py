import requests


class MongoLoaderClient:

    def __init__(self, mongo_loader_uri):
        self.mongo_loader_uri = mongo_loader_uri

    def send_to_mongo_loader(self, image_name: str, bin_file: bytes, sending: int):
        file_dict = {"file": (image_name, bin_file, "image.png")}
        try:
            response = requests.post(self.mongo_loader_uri, files=file_dict).text
            print(f"\nSuccess send number: {sending} \n\n{response}\n")
        except Exception as e:
            raise Exception(str(e))