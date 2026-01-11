pipeline {
    agent any // Se puede ejecutar en cualquier nodo/servidor disponible

    environment {
        // Definimos variables globales para la ejecución
        PYTHONPATH = "."
    }

    stages {
        stage('Checkout') {
            steps {
                // Descarga el código del repositorio Git
                checkout scm
            }
        }

        stage('Unit Tests') {
            steps {
                // Aquí es donde lanzas lo que practicamos antes
                sh 'pytest --cov=src --cov-report=term-missing'
            }
        }
    }

    post {
        always {
            // Limpieza: borra el directorio de trabajo al terminar para no dejar basura
            deleteDir()
        }
    }
}