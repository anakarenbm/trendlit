pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:3.7-alpine'
        }
      }
      steps {
        sh 'python3 -m unittest tests/test_compiled_code.py'
      }
    }

    stage('Build') {
      agent any
      steps {
        sh 'scripts/docker_build.sh'
      }
    }

    stage('Push') {
      agent any
      steps {
        script {
          docker.withRegistry('', 'docker_hub') {
            try {
              sh 'scripts/docker_check.sh'
              sh 'scripts/docker_push.sh'
            } catch (Exception e) {
              currentBuild.result = 'FAIL'
              error 'echo check that the intended version is already bumped'
              exit 1
            }
          }
        }
      }
    }
    stage('Remove') {
      agent any
      steps {
        script {
            sh 'scripts/docker_rmi.sh'
        }
      }
    }
  }
}