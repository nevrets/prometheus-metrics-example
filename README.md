## Usage

```
# 이미지 빌드 및 푸쉬
podman build --no-cache -t image-tag .
podman push image-tag

# kubernetes 배포
kubectl apply -f deployment.yaml -n namcespace
kubectl apply -f servicemonitor.yaml -n namespace

```
