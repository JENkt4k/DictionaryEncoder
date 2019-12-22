pipeline {
  agent { 
    docker {
       image 'python' 
    }
  }
  stages {
    stage('clean') {
      steps {
          sh './pyc.sh ./'  
      }
    }
    stage('build') {
      steps {
          sh 'pip install -r ./requirements.txt'
      }
    }
    stage('Unit Test'){
      parallel {
        stage('pytest'){
          steps{
            dir('DictionaryEncoder') {
              script {
                try {
                  sh 'py.test --junitxml ../test-reports/results-test_morse-$BUILD_NUMBER.xml ../tests/test_morse.py'
                  sh 'py.test --junitxml ../test-reports/results-test_DictionaryEncoder-$BUILD_NUMBER.xml ../tests/test_DictionaryEncoder.py'
                  sh 'py.test --junitxml ../test-reports/results-test_MorseCodeDictionaryEncoder-$BUILD_NUMBER.xml ../tests/test_MorseCodeDictionaryEncoder.py'
                } catch (Exception e) {
                  echo e.getMessage()
                  echo "pytest failed"
                }
              } 
            }    
          }
        }
        stage('coverage'){
          steps{
            dir('test-reports') {
              script {
                try {
                  sh 'coverage erase'
                  sh 'coverage run -m unittest discover -s ../tests'
                  sh 'coverage xml -i'
                } catch (Exception e) {
                  echo e.getMessage()
                  echo "coverage failed"
                }
              } 
            }    
          }
        }
      }
    }
    stage('Sonarqube') {
      environment {
        scannerHome = tool 'SonarQubeScanner'
      }
      steps {
        withSonarQubeEnv('sonarqube') {
          sh "${scannerHome}/bin/sonar-scanner"
        }
        timeout(time: 30, unit: 'MINUTES') {
          waitForQualityGate abortPipeline: true
        }
      }
    }
  }
  post {
    always {            
      archiveArtifacts 'test-reports/*.xml'
      junit 'test-reports/*.xml'
      dir('test-reports'){ 
        deleteDir()
      }      
    }
  }
} 