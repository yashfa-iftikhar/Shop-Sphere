pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'shop-sphere-jenkins'
        COMPOSE_FILE = 'docker-compose.yaml'
        REPO_URL = 'https://github.com/yashfa-iftikhar/Shop-Sphere'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: "${env.REPO_URL}"
            }
        }

        stage('Pre-Cleanup') {
            steps {
                echo 'Cleaning up old containers and volumes (if any)...'
                sh '''
                    docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE down --volumes || true
                    docker system prune -af || true
                    docker volume prune -f || true
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker containers...'
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE build --no-cache'
            }
        }

        stage('Check Frontend Output') {
            steps {
                echo 'Verifying frontend build output...'
                sh 'ls -lah my-project/dist || echo "Dist folder not found!"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting up containers...'
                sh 'docker-compose -p $COMPOSE_PROJECT_NAME -f $COMPOSE_FILE up -d'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running Selenium tests in Docker...'
                dir('tests') {
                    sh '''
                        docker build -t selenium-test .
                        docker run --rm selenium-test
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
