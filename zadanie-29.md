Generowanie szablonu konfiguracji Jenkins (JCasC)

 Co zawiera plik `jenkins-casc.yaml`

Plik `jenkins-casc.yaml` definiuje konfigurację Jenkinsa w formacie YAML zgodnie z podejściem "Configuration as Code (JCasC)".


Zakres konfiguracji

- **Podstawowe ustawienia Jenkinsa:**
  - 4 wykonawców (`numExecutors`)
  - 2 próby checkout SCM
  - Okres oczekiwania (quietPeriod) – 5 sekund

- **Globalne narzędzia:**
  - Maven 3.8.6
  - Node.js 18
  - Docker (tylko deklaracja)

- **Zadanie typu pipeline:**
  - Pipeline z trzema etapami: Build, Test, Deploy

- **Zmienne środowiskowe:**
  - JAVA_HOME i NODE_HOME

---


Jak użyć tej konfiguracji w Jenkinsie

### Krok 1: Przygotuj środowisko

1. **Upewnij się, że masz zainstalowane:**
   - Docker lub Jenkins na hoście
   - Plugin: **Configuration as Code Plugin** (`configuration-as-code`)

2. **Struktura katalogu:**

.
├── jenkins_home/
│ └── casc_configs/
│ └── jenkins-casc.yaml

bash
Kopiuj
Edytuj


Krok 2: Uruchom Jenkins z konfiguracją

#### Przykład z Docker:

```bash
docker run -d \
  --name jenkins-casc \
  -p 8080:8080 \
  -p 50000:50000 \
  -v $(pwd)/jenkins_home:/var/jenkins_home \
  -e CASC_JENKINS_CONFIG=/var/jenkins_home/casc_configs/jenkins-casc.yaml \
  jenkins/jenkins:lts
