# DSpyce-Demo-Application

[![CI](https://github.com/deeagle/dspyce-demo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/deeagle/dspyce-demo-app/actions/workflows/ci.yml)
[![Release version](https://github.com/deeagle/dspyce-demo-app/actions/workflows/release.yml/badge.svg)](https://github.com/deeagle/dspyce-demo-app/actions/workflows/release.yml)
[![Cronjobs](https://github.com/deeagle/dspyce-demo-app/actions/workflows/wf-cron.yml/badge.svg)](https://github.com/deeagle/dspyce-demo-app/actions/workflows/wf-cron.yml)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://hub.docker.com/r/docdee/dspyce-demo-app)
[![dspyce:0.0.3](https://img.shields.io/badge/dspyce-0.0.3-blue)](https://img.shields.io/badge/dspyce-0.0.3-blue)

A demo implementation of the DSpace API wrapper **DSpyce** as a containerized application,
created during OpenRepositories 2024 in Gothenburg.

## Run demo

- `docker run docdee/dspyce-demo-app:latest`

## Build and run locally

- `docker buildx build -t "dspyce-demo:local" .`
- `docker run dspyce-demo:local`

## Dependency management

With the update from dspyce `v0.0.2` to `v0.0.3` the build fails with a missing dependency error.

The Python community seems to solve this by merging multiple `requirements.txt` files.
I'm not sure how Dependabot will handle this, so I'm resolving it with the script `run-sync-requirements.sh` manually.

**Process:**

- retrieve DSpyce dependencies from the main project (`dspyce-requirements.txt`)
- merge with DSpyce demo app dependencies (`dspyce-demo-app-requirements.txt`)
- store the merge in file `requirements.txt`

## Weblinks

- [DSpace](https://dspace.lyrasis.org/)
- [DSpace (GitHub)](https://github.com/DSpace/DSpace)
- [DSpyce (GitHub)]

[DSpyce (GitHub)]: https://github.com/dspace-unimr/dspyce
