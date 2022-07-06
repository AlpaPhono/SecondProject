
#!/bin/bash
. ~/.bashrc
 
docker-compose build
 
docker push 
  
docker push aalphonso/qa2:name-generator-front
docker push aalphonso/qa2:name-generator-prefix
docker push aalphonso/qa2:name-generator-suffix
docker push aalphonso/qa2:name-generator-genre

docker stack deploy --compose-file docker-compose.yaml namegenerator