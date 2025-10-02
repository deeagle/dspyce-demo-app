PHONY: ci dbuild drun update-dependencies

DOCKER_LOCAL_NAME=dspyce-demo:local

dbuild:
	docker buildx build -t "${DOCKER_LOCAL_NAME}" --load .

drun:
	docker run --rm "${DOCKER_LOCAL_NAME}"

ci:
	./run-ci.sh

update-dependencies:
	./run-sync-requirements.sh