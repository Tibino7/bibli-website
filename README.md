# bibli-website

The purpose of this project is to deploy a complete library orchestration website on top of a Kubernetes architecture. 

### Deployment
#### Docker

##### From docker hub
You can directly run this project using images from docker hub:
For the database:
`docker run --name bibli-database  -e POSTGRES_DB=books -e POSTGRES_USER=tibino7 -e POSTGRES_PASSWORD=toto postgres:12.2 `
For the ISBN runtime:
`docker run --name bibli-isbn-service tibino7/isbnsrv:1.1.1 `
For the webapp:
`docker run --name bibli-website -p 8080:8080 tibino7/bibli-website:1.0 `

##### Build locally
You can also build the image locally.

Prerequisites: 
- have a running postgresql container, for example with:    
`docker run --name bibli-database  -e POSTGRES_DB=books -e POSTGRES_USER=tibino7 -e POSTGRES_PASSWORD=toto postgres:12.2 `
- have a running isbnsrv container, using [xlcnd's isbnlib as a microservice](https://github.com/xlcnd/isbnsrv)    

To deploy with docker:    
`make release`

or:    
`docker build --build-opts <your-build-options> -t bibli-website:1.0 .`    
`docker run --name <container-name> -p <port>:8000 bibli-website:1.0`

#### Kubernetes
Prerequisites:
- Kubernetes v1.7 or newer
- Helm package manager (tested with helm v3)
- Have local images of bibli-website (see above) and [xlcnd's isbnlib as a microservice](https://github.com/xlcnd/isbnsrv)    

To deploy using helm package manager:    
`cd chart`

`helm install -f bibli-website/values.yaml <release-name> bibli-website`

### Status
2021-01-12: Docker images published on tibino7 dockerhub repository
2020-05-12: Helm chart released    
2020-05-11: Database schema done    
2020-05-06: Front-End static structure of library page almost done. 