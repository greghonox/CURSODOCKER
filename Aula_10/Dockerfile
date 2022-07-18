FROM python:3

RUN apt-get update; apt-get upgrade -y; apt-get install python3-pip python3-dev -y

WORKDIR /app

RUN pip install flask

COPY . .

EXPOSE 5001

CMD ["python", "./app.py"]