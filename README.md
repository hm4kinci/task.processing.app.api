### BACKEND API

This api communicates with other services to serve requests received from frontend

In order to run the backend api below services should be up and running.
- service:classification 
- service:tagger
- database:mongo


### RUNNING API ###

- uses Python >= 3.8

`Development/Virtual Environment`: 
- $pip install -r requirements.txt
- refer settings.py file if configuration is needed
- $python app.py
 
`Docker`
- $docker-compose build
- $docker-compose up
- refer docker-compose.yaml if configuration needed. 
- requires **task-network** docker network to communicate with other services. 
- to create: $docker network create task-network
- to remove: $docker network rm my-net