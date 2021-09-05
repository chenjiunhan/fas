FROM ubuntu:20.04
EXPOSE 10000

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN apt-get install -y libssl-dev
RUN apt-get install -y openssl
RUN python3 -m pip install --upgrade pip
RUN pip install fastapi 
RUN pip install uvicorn 
RUN pip install pandas 
RUN pip install requests
RUN pip install python-multipart
RUN pip install schedule

WORKDIR /app
CMD ["python3", "-u", "server.py"]