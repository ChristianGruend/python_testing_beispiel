pipeline {
    agent any

    stages {
        // stage('Setup') {
        //     steps {
        //         sh 'apt-get update'
        //         sh 'apt install -y python3'
        //         sh 'apt install -y python3-pip'
        //         sh 'pip install pipx'
        //     }
        // }
        stage('Build') {
            steps {
                sh 'python3 ops.py'
            }
        }
        stage('Testing file') {
            steps {
                sh "python3 -m pytest"
            }
        }
        stage('Deliver') {
            steps {
                echo "Deliver...."
            }
        } 
    }
}
