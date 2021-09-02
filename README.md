# crud_test_task

## Prerequsites
Developed and tested in Linux (Ubuntu) environment only. Requires `git`, `docker` and `docker-compose` version 1.29 or higher to be installed. 

## Project setup and dev server
```
git clone 
cd ./crud_test_task
docker-compose --profile test --profile runserver -f dc-start.yml build
docker-compose --profile runserver -f dc-start.yml up
```
### Autotesting
```
docker-compose --profile test -f dc-start.yml up
```

## API reference
API reference is available at `/swagger`