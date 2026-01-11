# Use a lightweight Python image
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for C++ extensions (required for some ML libs)
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Run with Uvicorn (reflecting your knowledge of high-concurrency Python)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]