pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t hello-world-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop hello-world-container || true
                docker rm hello-world-container || true

                docker run -d \
                  --name hello-world-container \
                  -p 5000:5000 \
                  hello-world-app:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}
