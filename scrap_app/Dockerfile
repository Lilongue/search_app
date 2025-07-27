# scrap_app/Dockerfile
FROM python:3.9-slim
RUN apt-get update && apt-get install -y chromium
COPY chromedriver /usr/local/bin/chromedriver
RUN pip install selenium flask
COPY src app
CMD ["python", "app/main.py"]