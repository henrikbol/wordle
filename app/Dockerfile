FROM python:3.9-slim-buster

RUN /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

#COPY src/data/ ./data
COPY src/ ./
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080" ]