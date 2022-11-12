FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["pytest"]
CMD ["-vv"]