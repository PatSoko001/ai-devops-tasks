Analiza i poprawa istniejącego Jenkinsfile

Wykryte błędy w oryginalnym pliku

1. **Błąd literówki `stesp` → `steps`**
   - Sekcja `stage('Build')` zawiera literówkę – `stesp` zamiast `steps`.

2. **Niepoprawna komenda `npm build`**
   - Nie istnieje domyślna komenda `npm build`. W większości projektów Node.js należy użyć `npm run build`.

3. **Brak `withCredentials` przy publikowaniu obrazu Docker**
   - Dane logowania do Docker registry nie są zabezpieczone – powinny być obsłużone za pomocą `withCredentials`.

4. **Brak zmiennych środowiskowych dla nazwy/tagu obrazu**
   - Warto używać zmiennych `IMAGE_NAME` i `IMAGE_TAG` dla czytelności i łatwości edycji.

5. **Kolejność `when` i `steps` w `stage('Deploy')`**
   - W poprawnej składni deklaratywnej `when` powinien znajdować się przed `steps`.


Poprawki wprowadzone w `Jenkinsfile-fixed`

- Zmieniono `stesp` → `steps`
- Zmieniono `npm build` → `npm run build`
- Dodano sekcję `environment` z `IMAGE_NAME` i `IMAGE_TAG`
- Dodano `withCredentials` do bezpiecznego logowania do Docker Hub
- Poprawiono składnię bloku `when`
- Dodano logowanie z użyciem `docker login` i `--password-stdin`


Refleksja

Ten przykład pokazuje, jak nawet małe błędy (np. literówka) mogą uniemożliwić działanie całego pipeline'u. Dodatkowo warto stosować dobre praktyki jak:
- hermetyzacja danych w zmiennych środowiskowych
- ochrona poświadczeń przez Jenkins Credentials Manager
- stosowanie komend zgodnych z `package.json` (`npm run`)

Pipeline po poprawkach jest nie tylko działający, ale też bardziej bezpieczny i łatwy w utrzymaniu.
