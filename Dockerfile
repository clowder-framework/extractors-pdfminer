FROM python:3.10

COPY extractor-pdfminer.py requirements.txt extractor_info.json ./

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR ./
ENV PYTHONPATH=./

CMD ["python3", "extractor-pdfminer.py", "--heartbeat", "40"]
