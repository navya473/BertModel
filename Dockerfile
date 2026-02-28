FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the API
CMD ["uvicorn", "bert_api:app", "--host", "0.0.0.0", "--port", "8000"]
