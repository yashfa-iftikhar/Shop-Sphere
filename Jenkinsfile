pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/umer-5/Shop-Sphere.git'
            }
        }
        stage('Build with Docker Compose') {
            steps {
                sh 'docker-compose -p shop-sphere-jenkins -f docker-compose.yaml build'
            }
        }
        stage('Run Containers') {
            steps {
                sh 'docker-compose -p shop-sphere-jenkins -f docker-compose.yaml up -d'
            }
        }
    }
    post {
        always {
            sh 'docker-compose -p shop-sphere-jenkins -f docker-compose.yaml down || true'
        }
    }
}