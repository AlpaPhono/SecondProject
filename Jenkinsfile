pipeline {
    agent any
    environment {
       DH_USN = credentials('DH_USN')
       DH_PWD = credentials('DH_PWD')
    }
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash scripts/test.sh"
            }
        }
        stage('build, and push ') {
            steps {
                git branch: 'nameGenerator', url: 'https://github.com/AlpaPhono/SecondProject.git'
                sh "docker-compose build"
                sh "docker login --username ${DH_USN} --password ${DH_PWD}"
                sh "docker-compose push"
            }
        }
        stage('swarm deploy ') {
            steps {
            
                sh 'ssh Kaobi@10.154.0.5 "docker stack deploy --compose-file /home/Kaobi/docker-demos/prize-generator/docker-compose.yaml namegenerator"'
                sh''
            }
        }
    }
}

