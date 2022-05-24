# Building-image-deploy-Flask-REST API-using-docker

### Create Docker-Image :  
docker build . -f Dockerfile.dockerfile -t rojimage

### Run
docker run -it -p  9999:9999 rojimage:latest

### close the container:docker
cls

### Host container in the different hosts
docker run -it -p  6666:9999 rojimage:latest



### push container to the dockerhub-repository

1. docker tag rojimage:latest rojimage:143  (---Change Tag name if required else skip this step----)
2. Create repository in the Docker account
3. Login using docker credentials  :  docker login -u rojsun25 -p <password>
4. docker push rojsun25/rojimage:143

### Pull image from docker
docker pull rojsun25/rojimage  

  
### Mount local storage to Docker Storage/Volume 
{path)> docker run -it -p  9999:9999 -v <respective-path> :/rojimage save
##### For example: D:\image\save>docker run -it -p  9999:9999 -v D:\image\test\:/rojimages save
