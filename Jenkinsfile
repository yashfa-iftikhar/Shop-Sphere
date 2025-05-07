pipeline {
    agent any
    environment {
        COMPOSE_PROJECT_NAME = 'shop-sphere-jenkins'
        COMPOSE_FILE = 'docker-compose.yaml'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/umer-5/Shop-Sphere.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE up -d'
            }
        }
    }
    post {
        always {
            echo 'Stopping containers...'
            sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE down || true'
        }
    }
}

