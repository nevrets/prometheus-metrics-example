FROM python:3.9-slim-buster

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir  -r requiremenst.txt

# Expose port 8000 for the FastAPI application
EXPOSE 80
# Expose port 8090 for the prometheus metrics
EXPOSE 8090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
