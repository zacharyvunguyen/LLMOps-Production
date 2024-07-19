# Commands used in the Hands On
```
docker --version
docker pull nginx
docker images
docker run -d -p 8080:80 nginx
docker ps
docker stop <container_id>


docker build -t custom-nginx .
docker tag custom-nginx zacharynguyen/custom-nginx
docker push zacharynguyen/custom-nginx
```