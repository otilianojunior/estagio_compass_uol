FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /etapa-1

COPY . .

CMD [ "python", "carguru.py"]