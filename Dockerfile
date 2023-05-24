FROM python:alpine as builder
WORKDIR /app
COPY ./ .
RUN pip install -r requirements.txt
CMD ["python", "-u", "new_upload.py"]
