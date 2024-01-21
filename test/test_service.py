from fastapi.testclient import TestClient
from PIL import Image
from service import app

client = TestClient(app)

def test_segment_image_ok():
    files = {"image_file": ("test_image.png", open("resources/dog.jpg", "rb"), "image/png")}
    response = client.post("/segment-image/", files=files)
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    
def test_segment_image_fail():
    files = {"image_file": ("invalid-input.txt", open("resources/invalid-input.txt", "rb"), "text/plain")}
    response = client.post("/segment-image/", files=files)
    assert response.status_code == 400

    files = {"image_file": ("test_image.png", open("resources/dog.jpg", "rb"), "image/png")}
    response = client.post("/invalid-endpoint/", files=files)
    assert response.status_code == 404

    response = client.post("/segment-image/")
    assert response.status_code == 422

    response = client.get("/segment-image/")
    assert response.status_code == 405

    


