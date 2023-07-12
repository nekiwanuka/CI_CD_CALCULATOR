pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t  .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run calculator_app python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -p 8000:8000 calculator_app'
            }
        }
    }
}
