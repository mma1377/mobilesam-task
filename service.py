import io
import mimetypes
import asyncio
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from main import segment_everything
from PIL import Image

app = FastAPI()

'''
The segment_everything_async function is used to prevent the service from being blocked.
'''
async def segment_everything_async(image):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, segment_everything, image)

'''
Endpoint to accept image uploads, process them with the MobileSam segmentation model, and return the segmentation result.
'''
@app.post("/segment-image/")
async def segment_image(image_file: UploadFile = File(...)):
    # Check if the uploaded file is an image
    if not image_file.content_type.startswith('image'):
        raise HTTPException(status_code=400, detail="Wrong input! The input must be image.")

    image = Image.open(image_file.file).convert("RGB")
    fig = await segment_everything_async(image)
    
    # Save the segmentation result as PNG and prepare it for streaming
    buffer = io.BytesIO()
    fig.save(buffer, format='png')
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
