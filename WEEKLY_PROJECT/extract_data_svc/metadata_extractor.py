from PIL import Image
import os


class MetadataExtractor:

    @staticmethod
    def extract_metadata(file_path):
        with Image.open(file_path) as img:
            image_data = {
                "width": img.width,
                "height": img.height,
                "format": img.format,
                "file_size_bytes": os.path.getsize(file_path)
                }
        return image_data