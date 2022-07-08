#!/bin/bash
copy over compose fiile to swarm manager
copy over nginx conf file to swarm manager
docker stack deploy --compose-file docker-compose.yaml namegenerator
