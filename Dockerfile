FROM python:alpine

WORKDIR /app
COPY requirments.txt /app
RUN pip install -r requirments.txt
COPY . /app
CMD python malicious.py