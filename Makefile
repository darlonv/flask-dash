
DOCKER_IMAGE = darlon/flask-dash
PROJECT_NAME = flask-dash

run:
	docker compose up -d

terminal:
	docker exec -it $(PROJECT_NAME) /bin/bash

term: terminal

bash:
	docker run -it -v "$(PWD):/data" -p 5000:5000 -e FLASK_APP="flaskblog.py" -w /data/Flask_blog $(DOCKER_IMAGE) /bin/bash

build:
	docker build -t $(DOCKER_IMAGE) .

multi-build:
	docker buildx build  --output=bin --platform=linux/amd64,linux/arm64 -t $(DOCKERHUB_USER)/$(DOCKER_IMAGE) --push .

push:
	docker push $(DOCKER_IMAGE)

ps:
	docker compose ps

stop:
	docker compose stop

remove: stop
	docker compose rm -f

rm: remove

all: run

.PHONY: run build multi-build push ps stop remove%