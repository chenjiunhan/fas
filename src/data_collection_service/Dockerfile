FROM ubuntu:20.04
EXPOSE 10000

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip install fastapi uvicorn

WORKDIR /app
CMD ["python3", "server.py"]