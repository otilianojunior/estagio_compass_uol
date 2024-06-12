FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /etapa-2

COPY ../etapa-2 .

CMD [ "python", "ConverteStringHash.py"]