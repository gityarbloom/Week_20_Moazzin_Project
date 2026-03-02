import requests


class OCREngine:

    def __init__(self, ocr_uri):
        self.ocr_uri = ocr_uri

    def get_extracted_text(self, image_path):
        with open(image_path, "rb") as f:
            response = requests.post(self.ocr_uri, files={"file": f})
        return response.json()