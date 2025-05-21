from fastapi import FastAPI
from prometheus_client import start_http_server, Counter

METRIC_PORT = 8090

app = FastAPI()
start_http_server(METRIC_PORT)

# Define a Prometheus counter to track the number of requests
REQUEST_COUNTER = Counter('hello_world_requests', 'Number of requests to hello_world API')

@app.get("/")
async def root():
    # Increment the counter for each request
    REQUEST_COUNTER.inc()
    return {"msg": "helloworld"}
