FROM python:3.6-buster
RUN apt-get update
COPY simp.txt .
COPY simpAPP.py .
RUN pip install -r simp.txt
RUN mkdir /files
CMD gunicorn --workers=25 --bind=0.0.0.0:9999 --timeout=3 simpAPP:APP