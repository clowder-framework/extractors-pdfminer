FROM python:3.10

COPY pdfminer_extractor.py requirements.txt extractor_info.json ./

RUN pip install -r requirements.txt --no-cache-dir

WORKDIR ./

CMD ["python", "pdfminer_extractor.py", "--heartbeat", "40"]
