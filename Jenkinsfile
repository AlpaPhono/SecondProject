pipeline{
    agent any
    stages {
        stage("Enable my scripts folder as executable") {
            steps {
               git branch: 'namegenerator', url: 'https://github.com/AlpaPhono/SecondProject.git'
               sh "bash scripts/test.sh"
        }
        stage("test") {
            steps {
               git branch: 'namegenerator', url: 'https://github.com/AlpaPhono/SecondProject.git'
               sh "./script/test.sh"
            }
        }
         stage("build and push") {
            steps {
                //add git branch repo
               sh "./script/build.sh"
            }
        }
        // stage(' Prepair enviornment') {
        //     steps{
        //         sh './script/installation.sh'
        //         sh './script/ansible.sh'
        //     }
        // }    
        stage('depoly application through docker compose') {
            steps{
                // add git branch repo
                sh './script/deploy_app.sh'   
            }
        }
    }
}
}