from fastapi import FastAPI
from prometheus_client import start_http_server, Counter, Gauge
import time
import psutil
import os

METRIC_PORT = 8090

app = FastAPI()
start_http_server(METRIC_PORT)

# Define metrics
REQUEST_COUNTER = Counter('hello_world_requests', 'Number of requests to hello_world API')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU usage in percent')
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Memory usage in bytes')

def update_system_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.Process(os.getpid()).memory_info().rss)

@app.get("/")
async def root():
    # Increment the counter for each request
    REQUEST_COUNTER.inc()
    update_system_metrics()
    return {"msg": "helloworld"}

@app.get("/load")
async def generate_load():
    start_time = time.time()
    # CPU 부하 생성
    while time.time() - start_time < 5:  # 5초 동안 CPU 부하
        _ = [i * i for i in range(1000)]
    update_system_metrics()
    return {"msg": "CPU load generated"}
