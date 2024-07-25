FROM python:3.8-buster

RUN apt update -y && apt install awscli -y
COPY . /app 

WORKDIR /app 
RUN pip install -r requirements.txt 

CMD ['python' , 'app.py']

