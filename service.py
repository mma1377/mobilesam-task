import os
import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from main import segment_everything
from PIL import Image

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/segment-image/")
async def segment_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    output_path = "generated/output.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig = segment_everything(image);
    buffer = io.BytesIO()
    fig.save(buffer, format='png')
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")
