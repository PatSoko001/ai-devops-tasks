 Zadanie 9: Sprawdzanie poprawności pliku konfiguracyjnego

##  Oryginalny plik YAML


yaml

services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD=password


 Błędy w pliku YAML
Brak dwukropka po ports w sekcji app:
W linii, gdzie definiowane są porty dla usługi app, brakuje dwukropka (:) po ports. Powinna to być klucz-wartość, a nie tylko lista.


 Poprawiona wersja pliku YAML
yaml
Copy
Edit
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports: 
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password

 Podsumowanie
W oryginalnym pliku YAML zabrakło dwukropka po ports w sekcji app, co powodowało błąd składniowy. Poprawiona wersja pliku zawiera poprawny zapis.
