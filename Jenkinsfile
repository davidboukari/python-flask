node('all')
{

  stage('GIT')
  {


  }

  stage('Unit Tests')
  {
    sh 'pip install --upgrade --user tox'
    sh 'tox -r'
  }

  stage('Security Tests')
  {
    sh 'tox -r -e envsecurity'
  }

  stage('Quality Check Sonar')
  {

  }

  stage('Deployment')
  {
    // DEV

    // UAT

    // PRD
  }

}