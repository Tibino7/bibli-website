# bibli-website

The purpose of this project is to deploy a complete library orchestration website on top of a Kubernetes architecture. 

### Prerequisites:
A PostgreSQL database running, with database name, user and password matching with settings.py.    
Example with docker:
`docker run --name bibli-database  -e POSTGRES_DB=books -e POSTGRES_USER=tibino7 -e POSTGRES_PASSWORD=toto postgres:12.2 `

### Deployment
To deploy with docker:    
`make release`

or:    
`docker build --build-opts <your-build-options> -t bibli-website:1.0 .`

### Status
2020-05-11: Database schema done    
2020-05-06: Front-End static structure of library page almost done. 
