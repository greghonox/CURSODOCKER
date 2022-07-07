FROM python:3.11-rc-bullseye
WORKDIR /app

COPY requeriments.txt .

RUN apt update -y && apt install htop vim -y
RUN pip install --upgrade pip
RUN pip install -r requeriments.txt

CMD python3 main.py