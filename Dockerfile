FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]