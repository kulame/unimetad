pipeline {
  agent any
  stages {
    stage('检出') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: env.GIT_BUILD_REF]],
        userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]])
      }
    }
    stage('ci') {
      steps {
        script {
          sh 'docker login -u ${PKG_USER_NAME} -p ${PKG_PASSWORD} ${PKG_HOST}'
          docker.image("gengmei-docker.pkg.coding.net/tob/image/base").inside(){
            echo '构建中...'
            script{
              def exists = fileExists ".venv"
              if (!exists){
                sh "virtualenv .venv -p python3.8"
                sh "source .venv/bin/activate"
                sh "pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple"
                sh "pip install -r requirements.txt"
              }
              else {
                sh "source .venv/bin/activate"
              }
            }
            echo '格式化代码...'
            sh 'bash scripts/format'
            echo 'lint...'
            sh 'bash scripts/lint'
            echo "单元测试..."
            sh "bash scripts/test"
          }
        }

      }
    }
     stage("发布文档") {
         steps {
           script {
              docker.image("gengmei-docker.pkg.coding.net/tob/image/base").inside(){
                echo '生成 API 文档'
                sh 'apidoc -i app -o apidoc'
                echo '发布到 CODING API 文档'
                sh 'curl --fail -X POST -H "Authorization: token ${CODING_API_DOCS_DEPLOY_TOKEN}" -H "Accept:application/json" ${CODING_API_DOCS_DEPLOY_URL} -F "filename=@apidoc/api_data.json"'
                echo '完成.'
              }
           }
         }
     }
  }
}