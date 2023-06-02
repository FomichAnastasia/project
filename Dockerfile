FROM ubuntu+20.04
MAINTAINER st062944
RUN apt-get update -y
COPY . /opt/gsom_predictor
WORKDIR /opt/gsom_predictor
run apt install -y python3-pip
run pip install -r requirements.txt
cmd python3 app.py
