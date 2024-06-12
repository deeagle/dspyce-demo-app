# DSpyce-Demo-Application

[![CI](https://github.com/deeagle/dspyce-demo-app/actions/workflows/ci.yml/badge.svg)](https://github.com/deeagle/dspyce-demo-app/actions/workflows/ci.yml)
[![Release version](https://github.com/deeagle/dspyce-demo-app/actions/workflows/release.yml/badge.svg)](https://github.com/deeagle/dspyce-demo-app/actions/workflows/release.yml)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://hub.docker.com/r/docdee/dspyce-demo-app)
[![dspyce:0.0.2](https://img.shields.io/badge/dspyce-0.0.2-blue)](https://img.shields.io/badge/dspyce-0.0.2-blue)

A demo implementation of the DSpace API wrapper **DSpyce** as a containerized application,
created during OpenRepositories 2024 in Gothenburg.

## Run demo

- `docker run docdee/dspyce-demo-app:latest`

## Build and run locally

- `docker buildx build -t "dspyce-demo:local" .`
- `docker run dspyce-demo:local`

## Weblinks

- [DSpace](https://dspace.lyrasis.org/)
- [DSpace (GitHub)](https://github.com/DSpace/DSpace)
- [DSpyce (GitHub)]

[DSpyce (GitHub)]: https://github.com/dspace-unimr/dspyce
