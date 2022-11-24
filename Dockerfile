FROM python:3.9-alpine
WORKDIR /usr/src/app/favicon_script
COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3","favicon.py"]

