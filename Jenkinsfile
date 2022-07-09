pipeline {
    agent any
    environment {
       DLOGIN = credentials('DOCKER_LOGIN')
    }
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash scripts/test.sh"
            }
        }
    
        stage('Docker-login, build, and push ') {
                steps {
                    git branch: 'namegenerator', url: 'https://github.com/AlpaPhono/SecondProject.git'
                    sh '''docker-compose build
                    docker login --username $DLOGIN_USR --password $DLOGIN_PSW
                    docker-compose push'''
                }
            }
    }
}
