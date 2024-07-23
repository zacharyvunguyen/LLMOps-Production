
# Docker Hands-On Guide

This guide will walk you through the basic steps of working with Docker, including pulling images, running containers, building custom images, and pushing images to a Docker registry.

## Prerequisites

- Ensure Docker is installed on your system. You can download and install Docker from [here](https://www.docker.com/products/docker-desktop).

## Verify Docker Installation

To verify that Docker is installed and running on your system, check the version:

```sh
docker --version
```

## Pulling an Image

Download the official Nginx image from Docker Hub:

```sh
docker pull nginx
```

## Listing Docker Images

View the list of images you have on your local system:

```sh
docker images
```

## Running a Container

Run the Nginx container in detached mode and map port 8080 on your host to port 80 on the container:

```sh
docker run -d -p 8080:80 nginx
```

## Listing Running Containers

See the list of currently running containers:

```sh
docker ps
```

## Stopping a Container

Stop a running container by its container ID (replace `<container_id>` with the actual ID):

```sh
docker stop <container_id>
```

## Building a Custom Docker Image

Build a custom Docker image from a Dockerfile in the current directory and tag it as `custom-nginx`:

```sh
docker build -t custom-nginx .
```

## Running the Custom Image

Run the custom Docker image in detached mode and map port 8080 on your host to port 80 on the container:

```sh
docker run -d -p 8080:80 custom-nginx
```

## Tagging the Custom Image

Tag the custom image with your Docker Hub username (replace `zacharynguyen092` with your Docker Hub username):

```sh
docker tag custom-nginx zacharynguyen092/custom-nginx
```

## Pushing the Custom Image to Docker Hub

Push the tagged image to your Docker Hub repository (make sure you are logged in to Docker Hub):

```sh
docker push zacharynguyen092/custom-nginx
```

## Conclusion

You have now learned the basics of working with Docker, including pulling images, running containers, building custom images, and pushing images to a Docker registry. For more detailed information, refer to the [Docker documentation](https://docs.docker.com/).

```