# Building-image-deploy-Flask-REST API-using-docker

### Create Docker-Image :  
docker build . -f Dockerfile.dockerfile -t rojimage

### Run
docker run -it -p  9999:9999 rojimage:latest

### close the container:docker
cls

### Host container in the different hosts
docker run -it -p  6666:9999 rojimage:latest
