include INFO

.PHONY: build release save run test

build:
	docker build $(DOCKER_BUILD_OPTS) -t $(IMAGE_NAME):$(TAG) .

save:
	docker save $(IMAGE_NAME):$(TAG) > ../images/$(IMAGE_NAME):$(TAG).tar

run:
	docker run --name $(CONTAINER) $(RUN_OPTS) $(IMAGE_NAME):$(TAG)
	sleep 10

test:
	docker cp bibli/books/templates/books/table.html bibli-website:/opt/bibli/books/templates/books/table.html

release: build run

default: build