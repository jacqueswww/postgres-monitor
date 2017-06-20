### Usage

Simple postgres TPS monitor, echos to stdout which Openshift pushes to
Kibana.

docker run -it --rm jacqueswww/postgres-monitor

### Environment Variables

Required:

DATABASE_NAME  
DATABASE_USER  
DATABASE_PASSWORD  
POSTGRESQL_SERVICE_HOST  
POSTGRESQL_SERVICE_PORT  

Optional:

REFRESH_TIME - defaults to 60  
