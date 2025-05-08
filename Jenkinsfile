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
                echo 'Building Docker containers...'
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE build --no-cache'
            }
        }
        stage('List Build Output') {
            steps {
                echo 'Checking frontend dist directory...'
                sh 'ls -lah my-project/dist || echo "Dist folder not found"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Starting containers...'
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE up -d'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE down || true'
        }
    }
}

