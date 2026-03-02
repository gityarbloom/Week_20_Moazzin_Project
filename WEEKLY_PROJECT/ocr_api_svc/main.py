from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
from io import BytesIO

app = FastAPI()

@app.post("/ocr")
async def run_ocr(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = Image.open(BytesIO(image_bytes)).convert("L")
    text = pytesseract.image_to_string(img, lang="eng")
    return {"text": text.strip()}