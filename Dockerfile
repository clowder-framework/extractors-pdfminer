FROM python:3.10

COPY extractor-pdfminer.py requirements.txt extractor_info.json ./

RUN pip3 install -r requirements.txt --no-cache-dir

WORKDIR ./

CMD ["python3", "extractor-pdfminer.py", "--heartbeat", "40"]
