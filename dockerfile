FROM python:3.11 AS base
RUN apt-get update && apt-get install -y \
    libgl1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt

FROM base AS testing
RUN pip install -r test/requirements.txt
CMD ["pytest"]

FROM base AS dev
EXPOSE 80
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "80"]