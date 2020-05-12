# bibli-website

The purpose of this project is to deploy a complete library orchestration website on top of a Kubernetes architecture. 

### Deployment
#### Docker
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

To deploy using helm package manager:    
`cd chart`

`helm install -f bibli-website/values.yaml <release-name> bibli-website`

### Status
2020-05-12: Helm chart released    
2020-05-11: Database schema done    
2020-05-06: Front-End static structure of library page almost done. 
