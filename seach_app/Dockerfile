# seach_app/Dockerfile
FROM python:3.12-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src app
EXPOSE 5020
CMD ["python", "app/main.py"]
