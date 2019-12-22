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
      archiveArtifacts 'DictionaryEncoder/test-reports/*.xml'
      junit 'DictionaryEncoder/test-reports/*.xml'
      dir('DictionaryEncoder/test-reports'){ 
        deleteDir()
      }      
    }
  }
} 