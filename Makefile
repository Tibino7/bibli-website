.PHONY: build run deploy

build:
	docker build --no-cache -t bibli-website:0.1.0 .

run:
	docker run --name bibli-website-0 -p 8000:8000 bibli-website:0.1.0

deploy: build run

default: build