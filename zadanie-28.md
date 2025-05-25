Skrypt do zarządzania zadaniami Jenkins


Jak działa skrypt

Skrypt `jenkins-manager.py` pozwala na interakcję z Jenkins poprzez jego API z użyciem biblioteki `python-jenkins`.

### Funkcjonalności:

1. **Listowanie zadań**  
   Używa `server.get_jobs()` by pobrać listę wszystkich zadań Jenkins.

2. **Status ostatniego builda**  
   Pobiera informacje o ostatnim buildzie danego zadania (`get_job_info`, `get_build_info`), w tym jego numer, wynik i URL.

3. **Uruchamianie zadania**  
   Używa `server.build_job()` do ręcznego zainicjowania builda.

### Autoryzacja

Skrypt loguje się do instancji Jenkins przy użyciu loginu i hasła lub tokena API. Dane te można zmienić w zmiennych `USERNAME` i `PASSWORD`.

### Obsługa błędów

Każda operacja otoczona jest blokiem `try/except`, co pozwala przechwytywać błędy i nie przerywać działania skryptu w razie problemów.


Wymagania

Zainstaluj bibliotekę:

```bash
pip install python-jenkins
