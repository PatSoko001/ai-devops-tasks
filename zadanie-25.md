Generowanie prostego Jenkinsfile

Cel

Celem tego zadania było stworzenie prostego pliku `Jenkinsfile` dla aplikacji Node.js. Pipeline miał zawierać następujące etapy:
- Pobranie kodu z repozytorium
- Instalacja zależności
- Uruchomienie testów
- Budowanie aplikacji
- Budowanie obrazu Docker
- Publikowanie obrazu do rejestru Docker

Wyjaśnienie etapów pipeline'u

stage('Checkout')
```groovy
checkout scm
