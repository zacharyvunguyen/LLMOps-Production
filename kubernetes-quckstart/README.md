
# Docker Hands-On Guide

This guide will walk you through the basic steps of working with Docker and Kubernetes, including pulling images, running containers, building custom images, pushing images to a Docker registry, and managing Kubernetes resources.

## Prerequisites

- Ensure Docker is installed on your system. You can download and install Docker from [here](https://www.docker.com/products/docker-desktop).
- Ensure Kubernetes (kubectl) is installed and configured to interact with your Kubernetes cluster. You can install kubectl from [here](https://kubernetes.io/docs/tasks/tools/).

## Docker Commands

### Verify Docker Installation

To verify that Docker is installed and running on your system, check the version:

```sh
docker --version
```

### Pulling an Image

Download the official Nginx image from Docker Hub:

```sh
docker pull nginx
```

### Listing Docker Images

View the list of images you have on your local system:

```sh
docker images
```

### Running a Container

Run the Nginx container in detached mode and map port 8080 on your host to port 80 on the container:

```sh
docker run -d -p 8080:80 nginx
```

### Listing Running Containers

See the list of currently running containers:

```sh
docker ps
```

### Stopping a Container

Stop a running container by its container ID (replace `<container_id>` with the actual ID):

```sh
docker stop <container_id>
```

### Building a Custom Docker Image

Build a custom Docker image from a Dockerfile in the current directory and tag it as `custom-nginx`:

```sh
docker build -t custom-nginx .
```

### Running the Custom Image

Run the custom Docker image in detached mode and map port 8080 on your host to port 80 on the container:

```sh
docker run -d -p 8080:80 custom-nginx
```

### Tagging the Custom Image

Tag the custom image with your Docker Hub username (replace `zacharynguyen092` with your Docker Hub username):

```sh
docker tag custom-nginx zacharynguyen092/custom-nginx
```

### Pushing the Custom Image to Docker Hub

Push the tagged image to your Docker Hub repository (make sure you are logged in to Docker Hub):

```sh
docker push zacharynguyen092/custom-nginx
```

## Kubernetes Commands

### Get All Pods

List all pods running in the cluster:

```sh
kubectl get pods
```

### Apply a Pod Configuration

Create a pod based on the configuration in `pod.yaml`:

```sh
kubectl apply -f pod.yaml
```

### Describe a Pod

Get detailed information about the pod named `myapp`:

```sh
kubectl describe pod myapp
```

### Apply a Service Configuration

Create a service based on the configuration in `svc-local.yaml`:

```sh
kubectl apply -f svc-local.yaml
```

### Get All Services

List all services running in the cluster:

```sh
kubectl get svc
```

### Describe a Service

Get detailed information about the service named `mysvc`:

```sh
kubectl describe svc mysvc
```

### Delete All Pods

Delete all pods in the cluster:

```sh
kubectl delete pods --all
```

### Delete All Services

Delete all services in the cluster:

```sh
kubectl delete svc --all
```

### List All API Resources

Get a list of all available API resources:

```sh
kubectl api-resources
```

### Get All Deployments

List all deployments in the cluster:

```sh
kebectl get deployments
```

### Apply a Deployment Configuration

Create a deployment based on the configuration in `deployment.yaml`:

```sh
kubectl apply -f deployment.yaml
```

### Describe Deployments

Get detailed information about all deployments:

```sh
kubectl describe deployments
```

### Check Rollout Status of a Deployment

Check the status of a deployment rollout:

```sh
kubectl rollout status deployment
```

### Create a ConfigMap

Create a ConfigMap named `app-config` with a key-value pair:

```sh
kubectl create configmap app-config --from-literal=DATABASE_URL="mysql://user:password@mysql-server:3306/db_name"
```

### Describe a ConfigMap

Get detailed information about the ConfigMap named `app-config`:

```sh
kubectl describe cm app-config 
```

### Execute a Command in a Pod

Execute a command inside a pod named `app-pod` (replace `app-pod` with the actual pod name):

```sh
kubectl exec -it app-pod -- /bin/bash
```

### Create a Secret

Create a secret named `db-secret` with a key-value pair:

```sh
kubectl create secret generic db-secret --from-literal=DB_PASSWORD=password123
```

### Execute a Command in a Different Pod

Execute a command inside a pod named `db-pod` (replace `db-pod` with the actual pod name):

```sh
kubectl exec -it db-pod -- /bin/bash
```

## Conclusion

You have now learned the basics of working with Docker and Kubernetes, including pulling images, running containers, building custom images, pushing images to a Docker registry, and managing Kubernetes resources. For more detailed information, refer to the [Docker documentation](https://docs.docker.com/) and the [Kubernetes documentation](https://kubernetes.io/docs/).

```