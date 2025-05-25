Zadanie 21: Transformacja danych

Cel

Przekształcenie danych z formatu JSON do CSV.

---

Dane wejściowe (JSON)

Zawierają listę użytkowników z polami:
- `id`: liczba
- `name`: ciąg znaków
- `email`: ciąg znaków
- `roles`: tablica ról

Zapisane w pliku `users.json`.

---

Dane wyjściowe (CSV)

Plik `users.csv` zawiera te same dane w postaci płaskiej tabeli z kolumnami:
- `id`
- `name`
- `email`
- `roles` (wartości połączone średnikiem, np. `admin;user`)

---

Wyzwania konwersji

- **Tablica w polu (`roles`)**: CSV nie obsługuje zagnieżdżonych struktur, dlatego zdecydowano się na konwersję tablicy ról do jednego ciągu znaków, gdzie role są oddzielone średnikiem `;`. To intuicyjny i czytelny sposób reprezentacji wielu wartości w jednym polu.
  
- **Zachowanie poprawności kodowania znaków**: W razie użycia znaków specjalnych (np. przecinków, cudzysłowów) należy pamiętać o ich odpowiednim escapowaniu.

---
Podsumowanie

Transformacja danych z JSON do CSV może być prosta, o ile odpowiednio zaplanuje się mapowanie struktur złożonych (jak tablice). W tym przypadku zastosowano konwersję tablicy `roles` do pola tekstowego z separatorami, co sprawdza się przy prostych przypadkach eksportu danych.
