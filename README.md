# Internship Take Home Assignment - Software Engineer

## How to Run the Code

1. **Create a Virtual Environment and Activate It**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Service**

    ```bash
    uvicorn service:app --host YOUR_HOST --port YOUR_PORT --reload
    ```
    Replace `YOUR_HOST` with the desired host address (e.g., localhost or 0.0.0.0) and `YOUR_PORT` with the desired port number.

4. **Interact with the service**
    You can interact with the service by using YOUR_HOST:YOUR_PORT/segment-image/ end-point
    The image should be send in request body as multi-body input with key as image_file and the vlue of type File and value the image file.
    
    The YOUR_HOST:YOUR_PORT/doc/ end point can be used on the browser to check how the service works and also test the service on web visually.

5. **install the Test Requirements**

    ```bash
    pip install -r test/requirements.txt
    ```
    (It is suggested different venv to be used for testing.)

6. **إRun the Test**

    Run this code while in the root directory of the project:

   ```bash
    pytest
    ```

## How to build Docker image and Run it

1. **Build Docker Image**

    ```bash
    docker build -t mobilesam/dev --target dev .
    ```

2. **Run the Container**

    ```bash
    docker run -p 4000:80 mobilesam/dev
    ```
   
Then the service will be served at 0.0.0.0:4000/segment-image/

At the next step, we can build and run the testing image

3. **Build Docker Testing Image**

    ```bash
    docker build -t mobilesam/testing --target testing .
    ```

4. **Run the Container**

    ```bash
    docker run mobilesam/testing 
    ```