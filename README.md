# Internship Take Home Assignment - Software Engineer

The goal of this project is to develop a FastAPI service for deploying the MobileSam segmentation model, containerize the service with Docker, and ensure efficient interaction with the model on the CPU.


## How to Run the Service

1. **Create a Virtual Environment and Activate It:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Requirements:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Service:**

    ```bash
    uvicorn service:app --host YOUR_HOST --port YOUR_PORT --reload
    ```
   Replace `YOUR_HOST` with the desired host address (e.g., localhost or 0.0.0.0) and `YOUR_PORT` with the desired port number.

4. **Interact with the Service:**
   To interact with the service, use the endpoint `YOUR_HOST:YOUR_PORT/segment-image/`. Send the image in the request body as a multi-part input with the key as `image_file` and the value as the image file.

   Additionally, you can use `YOUR_HOST:YOUR_PORT/doc/` in your browser to visually test the service.

5. **Install the Test Requirements:**

    ```bash
    pip install -r test/requirements.txt
    ```
   (It is suggested to use a separate virtual environment for testing.)

6. **Run the Tests:**

   Run this code while in the root directory of the project:

   ```bash
    pytest
    ```

## How to Build Docker Image and Run It

1. **Build Docker Image:**

    ```bash
    docker build -t mobilesam/dev --target dev .
    ```

2. **Run the Container:**

    ```bash
    docker run -p 4000:80 mobilesam/dev
    ```

The service will be served at `0.0.0.0:4000/segment-image/`. Follow the next steps to build and run the testing image.

3. **Build Docker Testing Image:**

    ```bash
    docker build -t mobilesam/testing --target testing .
    ```

4. **Run the Testing Container:**

    ```bash
    docker run mobilesam/testing 
    ```
