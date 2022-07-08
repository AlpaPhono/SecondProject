pipeline{
    agent any
    stages {
        stage("Enable my script folder to be executable") {
            steps {
                //add git branch repo
               sh "chmod +x ./scripts/*"
            }
        }
        stage("test") {
            steps {
                //add git branch repo
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