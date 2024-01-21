import io
import mimetypes
import asyncio
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from main import segment_everything
from PIL import Image

app = FastAPI()

async def segment_everything_async(image):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, segment_everything, image)

@app.post("/segment-image/")
async def segment_image(image_file: UploadFile = File(...)):
    if not image_file.content_type.startswith('image'):
        raise HTTPException(status_code=400, detail="Wrong input! The input must be image.")
    image = Image.open(image_file.file).convert("RGB")
    fig = await segment_everything_async(image)
    buffer = io.BytesIO()
    fig.save(buffer, format='png')
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")
