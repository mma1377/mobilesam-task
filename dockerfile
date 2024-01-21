FROM python:3.11
RUN apt-get update && apt-get install -y \
    libgl1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "80"]
