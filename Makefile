include INFO

.PHONY: build release save run

build:
	docker build $(DOCKER_BUILD_OPTS) -t $(IMAGE_NAME) .

save:
	docker save $(IMAGE_NAME):$(TAG) > ../images/$(IMAGE_NAME):$(TAG).tar

run:
	docker run --name $(CONTAINER) $(RUN_OPTS) $(IMAGE_NAME):$(TAG)
	sleep 10

release: build run

default: build