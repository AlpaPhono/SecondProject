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
        stage('build, and push ') {
            steps {
                git branch: 'namegenerator', url: 'https://github.com/AlpaPhono/SecondProject.git'
                sh "docker-compose build"
                sh "docker login --username $DLOGIN_USR --password $DLOGIN_PSW"
                sh "docker-compose push"
            }
        }
    }
}

