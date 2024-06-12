FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /etapa-3

COPY . .

CMD [ "python", "ConverteStringHash.py"]