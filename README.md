# crud_test_task

## Prerequsites
Developed and tested in Linux (Ubuntu) environment only. Requires `git` and `docker` to be installed. 

## Project setup and dev server
```
git clone 
cd ./crud_test_task
docker-compose -f dc-start.yml build
docker-compose -f dc-start.yml up
```
### Autotesting
`docker-compose -f dc-start.yml run django-autotests`

## API reference
API reference is available at `/swagger`