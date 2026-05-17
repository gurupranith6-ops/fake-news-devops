pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/gurupranith6-ops/fake-news-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fake-news-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop fake-news-container || true'
                sh 'docker rm fake-news-container || true'
                sh 'docker run -d --name fake-news-container -p 5000:5000 fake-news-app'
            }
        }

        stage('Test Application') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}
