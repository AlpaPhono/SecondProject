#!/bin/bash
docker-compose build
docker login --username --password
docker-compose push
