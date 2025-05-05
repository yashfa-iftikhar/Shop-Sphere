pipeline {
    agent any

    environment {
        COMPOSE_FILE = "docker-compose.yml"
        PROJECT_NAME = "mern_ci_pipeline"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/umer-5/Shop-Sphere.git'
            }
        }

        stage('Build & Run Containers') {
            steps {
                sh """
                docker-compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} down
                docker-compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} up -d --build
                """
            }
        }
    }

    post {
        always {
            echo '✅ Jenkins pipeline finished!'
        }
    }
}
