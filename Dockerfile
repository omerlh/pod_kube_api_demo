FROM python:alpine

WORKDIR /app
COPY . /app
RUN pip install -r requirments.txt

CMD python malicious.py