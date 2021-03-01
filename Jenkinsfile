pipeline
{
  agent any
  stages{
    stage('GIT')
    {
       steps
       { 
         echo 'Get the git source ...'
         sleep(2)         
       } 
    }
  
    stage('Unit Tests')
    {
      steps
      {
        echo 'Unit Tests...'
        #sh 'pip install --upgrade --user tox'
        sh 'tox -r'
      }
    }
  
    stage('Security Tests')
    {
      steps
      {
        echo 'Security Tests...'
        sleep(2)
        //sh 'tox -r -e envsecurity'
      }
    }
  
    stage('Sonarqube')
    {
      environment
      {
        scannerHome = tool 'SonarQubeScanner'
      }    
      steps
      {
        withSonarQubeEnv('sonarqube')
        {
          sh "${scannerHome}/bin/sonar-scanner"
        } 
        timeout(time: 10, unit: 'MINUTES')
        {
          waitForQualityGate abortPipeline: true
        }
      }
    }
  
    stage('Deployment')
    {
      steps
      {  
        echo 'Deployment...'
        sleep(2)
        // DEV
  
        // UAT
  
        // PRD
      }
    }
  
  }

}
