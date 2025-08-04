FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 5020

# Set the working directory to src
WORKDIR /app/src

# Run the application
CMD ["python", "main.py"]
