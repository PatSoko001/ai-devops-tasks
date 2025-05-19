Zadanie 4: Określanie roli w promptach

##  Prompt 1: Bez przypisania roli

**Użyty prompt:**
Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

yaml
Copy
Edit

**Wygenerowana odpowiedź:**
> Duże zużycie pamięci przez kontener Docker może być spowodowane błędami w aplikacji lub nieoptymalną konfiguracją. Aby rozwiązać ten problem:
> 
> 1. Sprawdź zużycie zasobów za pomocą `docker stats`.
> 2. Upewnij się, że kontener ma ustawione limity pamięci (`--memory`).
> 3. Przeanalizuj aplikację pod kątem wycieków pamięci.
> 4. Rozważ zmniejszenie buforów, cache lub danych ładowanych do RAM.
> 5. Użyj narzędzi monitorujących, np. Prometheus, aby śledzić zużycie.

---

##  Prompt 2: Z przypisaną rolą

**Użyty prompt:**
Jesteś doświadczonym DevOps Engineerem z 10-letnim doświadczeniem. Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

yaml
Copy
Edit

**Wygenerowana odpowiedź:**
> Jako DevOps Engineer z wieloletnim doświadczeniem, rekomenduję podejście warstwowe do diagnozowania i rozwiązywania problemów z pamięcią w kontenerach Docker:
> 
> 1. **Diagnostyka wstępna**: Uruchom docker stats lub docker container inspect, aby określić dokładny poziom zużycia RAM przez kontener.
> 2. **Zastosowanie limitów zasobów**: W produkcji zawsze ustawiam limity pamięci, np. --memory=512m oraz --memory-swap=1g , aby zapobiec niekontrolowanemu zużyciu.
> 3. **Debugowanie aplikacji**: Zidentyfikuj potencjalne memory leak’i – np. przy pomocy Valgrind (C/C++) lub --inspect i narzędzi profilujących dla Node.js/Python.
> 4. **Optymalizacja konfiguracji środowiska uruchomieniowego**: Upewnij się, że Garbage Collector (w JVM, Node.js itd.) działa zgodnie z oczekiwaniami; czasem wystarczy zmiana flag uruchomieniowych.
> 5. **Obserwacja historyczna**: Wdrożenie stacku monitorującego (np. Prometheus + Grafana, eBPF tools) umożliwia korelację wzorców zużycia pamięci z cyklem działania aplikacji.
> 6. **Przegląd warstwy hosta**: Warto sprawdzić również, czy host systemowy nie ogranicza zasobów (np. cgroups, konfiguracja systemd), co może wpływać na kontenery.

---

## Wnioski

| Kryterium                     | Prompt 1: Bez roli                | Prompt 2: Z przypisaną rolą DevOps Engineer |
|------------------------------|-----------------------------------|--------------------------------------------|
| **Szczegółowość**            | Podstawowa                        | Zaawansowana, warstwowa analiza            |
| **Język techniczny**         | Ogólny                            | Profesjonalny, precyzyjny                  |
| **Zakres narzędzi**          | Tylko Docker CLI                  | Docker, systemd, GC, Prometheus, eBPF      |
| **Perspektywa praktyczna**   | Raczej użytkownik końcowy         | Perspektywa doświadczonego inżyniera       |
| **Użyteczność w DevOps**     | Średnia                           | Bardzo wysoka                              |

🔍 **Wniosek końcowy**:  
Dodanie kontekstu roli (np. „doświadczony DevOps Engineer”) skutkuje odpowiedzią bardziej specjalistyczną, szczegółową i praktyczną. Taka technika znacząco zwiększa jakość generowanej treści, szczególnie w zadaniach wymagających wiedzy eksperckiej.

---
