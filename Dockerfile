FROM python:3.10

COPY extractor-pdfminer.py requirements.txt extractor_info.json ./

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR ./

CMD ["python", "--help", "--heartbeat", "40"]
