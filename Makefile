PHONY: ci dbuild drun fix-wsl update-dependencies

DOCKER_LOCAL_NAME=dspyce-demo:local

dbuild:
	docker buildx build -t "${DOCKER_LOCAL_NAME}" --load .

drun:
	docker run --rm "${DOCKER_LOCAL_NAME}"

ci:
	@if grep -qi microsoft /proc/version; then $(MAKE) fix-wsl; fi
	./run-ci.sh

fix-wsl:
	find . -iname "*.sh" -type f | xargs dos2unix

update-dependencies:
	./run-sync-requirements.sh
