FROM python:3.11.3-buster

WORKDIR /app

COPY . .

RUN mkdir /data
VOLUME [ "/data" ]

RUN pip install -r requirements.txt

CMD ["python3", "-u","main.py"]
