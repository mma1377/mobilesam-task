import os
from fastapi import FastAPI, File, UploadFile
from main import segment_everything
from PIL import Image

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

app = FastAPI()

@app.post("/segment-image/")
async def segment_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    output_path = "generated/output.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig = segment_everything(image);
    fig.save(output_path)
    return {"filename": file.filename}
