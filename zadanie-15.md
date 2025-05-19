Zadanie 15: Refaktoryzacja funkcji z wieloma if-else

Cel zadania
Zadaniem było uproszczenie funkcji getEnvironmentConfig, która pierwotnie korzystała z wielu instrukcji if-else do zwracania konfiguracji dla różnych środowisk.

 
 Opis refaktoryzacji
Zamiast stosować zagnieżdżone instrukcje warunkowe, zastosowano prostą strukturę danych w postaci obiektu (ENV_CONFIGS), która przechowuje konfiguracje dla poszczególnych środowisk (development, testing, staging, production).

Funkcja została skrócona do jednej linii, dzięki czemu:

javascript
Copy
Edit
return ENV_CONFIGS[env] || ENV_CONFIGS['development'];
Zwraca konfigurację odpowiadającą podanemu środowisku lub domyślnie konfigurację development, jeśli środowisko jest nieznane.



Korzyści płynące z refaktoryzacji
Czytelność – kod jest bardziej przejrzysty i łatwy do zrozumienia na pierwszy rzut oka.

Łatwość utrzymania – dodanie nowego środowiska (np. preview) wymaga tylko dodania nowego wpisu do obiektu ENV_CONFIGS, bez modyfikacji logiki funkcji.

Redukcja powtórzeń – unikamy powielania konfiguracji (np. ta sama konfiguracja dla development i wartości domyślnej).

Skalowalność – przy większej liczbie środowisk refaktoryzowana wersja jest znacznie bardziej skalowalna.


 
 Struktura plików po zadaniu
arduino
Copy
Edit
/projekt
  ├── config.js              // Oryginalna funkcja
  ├── config-refactored.js  // Refaktoryzowana wersja funkcji
  ├── zadanie-15.md         // Opis zmian i korzyści
