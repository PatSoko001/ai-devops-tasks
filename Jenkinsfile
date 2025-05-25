pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "myapp:latest"
    DOCKER_REGISTRY = "registry.example.com/myapp"
  }

  stages {
    stage('Checkout') {
      steps {
        echo "Cloning repository..."
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        echo "Installing Node.js dependencies..."
        sh 'npm install'
      }
    }

    stage('Run tests') {
      steps {
        echo "Running tests..."
        sh 'npm test'
      }
    }

    stage('Build app') {
      steps {
        echo "Building the application..."
        sh 'npm run build'
      }
    }

    stage('Build Docker image') {
      steps {
        echo "Building Docker image..."
        sh "docker build -t $DOCKER_IMAGE ."
      }
    }

    stage('Push Docker image') {
      steps {
        echo "Pushing Docker image to registry..."
        withCredentials([usernamePassword(credentialsId: 'docker-registry-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin registry.example.com"
          sh "docker tag $DOCKER_IMAGE $DOCKER_REGISTRY"
          sh "docker push $DOCKER_REGISTRY"
        }
      }
    }
  }

  post {
    always {
      echo "Pipeline finished."
    }
  }
}
