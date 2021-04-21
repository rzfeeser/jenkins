/* scripted pipeline is a general purpose DSL
    built with Groovy. Most of Groovy language is
    made avail with a scripted pipeline */
    
node {
  // the agent we wish to choose
    label 'java-docker-worker'
    stage('build') {
        def runme = 'top'  // define the var runme as top
        if ("${runme}" == 'top') {
            echo 'I only execute if runme is set to top'
        } else if ("${runme}" == 'main') {
            echo 'I would only execute if runme were set to main'
        } else {
            sh 'python3 --version'
        }
    }
}
