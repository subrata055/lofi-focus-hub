pipeline {
    agent any
    
    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }
    
    stages {
        stage('Verify') {
            steps {
                sh '''
                    docker version
                    docker compose version
                '''
            }
        }
        
        // stage('Clean') {
        //     steps {
        //         sh 'sh dockerclean.sh'
        //     }
        // }
        
        // stage('Sonarqube Scan') {
        //     steps {
        //         script {
        //             scannerHome = tool 'sonar-scanner'
        //         }
        //         withSonarQubeEnv('sonarqube-server') {
        //             sh "${scannerHome}/bin/sonar-scanner -X"
        //         }
        //     }
        // }
        
        // stage('Quality Gate') {
        //     steps {
        //         withSonarQubeEnv('sonarqube-server') {
        //             waitForQualityGate abortPipeline: true
        //         }
        //     }
        // }
        
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker compose kill'
                sh 'docker compose up -d'
            }
        }
    }
    
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
        success {
            echo 'Lo-Fi Focus Hub deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}