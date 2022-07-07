FROM python:3

RUN apt update; apt upgrade -y; apt install python3-pip python3-dev -y

WORKDIR /app

RUN pip install flask requests flask_mysqldb

COPY . .

EXPOSE 5001

CMD ["python", "./app.py"]
