pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                "C:\\Program Files\\Python314\\python.exe" -m pip install -r requirements.txt
                "C:\\Program Files\\Python314\\python.exe" -m pip install pytest pytest-html
                '''
            }
        }

        stage('Run testcases') {
            steps {
                bat '''
                if not exist reports mkdir reports
                "C:\\Program Files\\Python314\\python.exe" -m pytest testcases --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}
