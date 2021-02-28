pipeline
{
  agent any
  {
    stage('GIT')
    {
       steps
       { 
         echo 'Building...'
         sleep(2)         
       } 
    }
  
    stage('Unit Tests')
    {
      steps
      {
        echo 'Unit Tests...'
        sleep(2)
        //sh 'pip install --upgrade --user tox'
        //sh 'tox -r'
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
