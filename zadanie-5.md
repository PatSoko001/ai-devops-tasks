 Zadanie 5: Wizualizacja ASCII Art

## Prompt 1: Prosty diagram

**Użyty prompt:**
Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych.

markdown
Copy
Edit

**Wygenerowany diagram:**
+--------+ +----------------+ +-------------+
| Client | -----> | App Server | -----> | Database |
+--------+ +----------------+ +-------------+

yaml
Copy
Edit

---

##  Prompt 2: Ulepszony diagram z opisami

**Użyty prompt:**
Dodaj do diagramu opisy elementów i kierunki przepływu danych.

markdown
Copy
Edit

**Wygenerowany diagram:**
[Client]
|
| HTTP Request
v
+---------------+
| App Server |
| - Handles API |
| - Business logic
+---------------+
|
| SQL Query
v
+---------------+
| Database |
| - Stores data |
+---------------+

Legenda:
→ Dane przesyłane z góry na dół (Client → App Server → Database)

yaml
Copy
Edit

---

##  Wnioski

- **Diagram podstawowy**: Pierwszy prompt dał prostą, zwięzłą reprezentację relacji między komponentami, odpowiednią do szybkiego poglądu architektury.
- **Diagram ulepszony**: Drugi prompt z kontekstem spowodował dodanie etykiet przepływu danych i funkcjonalności komponentów, co zwiększa czytelność i wartość edukacyjną.
- **Wniosek końcowy**: Dodanie dodatkowych wymagań w promptach (np. opisów, kierunków przepływu) prowadzi do bogatszej i bardziej informacyjnej wizualizacji. ASCII Art może być efektywnym sposobem szybkiego przedstawiania architektury w dokumentacji technicznej.

---
