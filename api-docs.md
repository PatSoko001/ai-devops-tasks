API Documentation


Endpoint: GET /api/users

Zwraca listę użytkowników z opcjonalnym filtrowaniem i paginacją.


Parametry zapytania

| Nazwa   | Typ     | Wymagany | Domyślna wartość | Opis |
|---------|----------|----------|------------------|------|
| page    | integer  | nie      | 1                | Numer strony wyników |
| limit   | integer  | nie      | 10               | Liczba wyników na stronę (maksymalnie 100) |
| role    | string   | nie      | —                | Filtruje użytkowników według roli |

---

Przykładowe żądanie


GET /api/users?page=2&limit=5&role=admin HTTP/1.1
Host: example.com


Przykładowa odpowiedź

json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "page": 2,
  "limit": 5,
  "total": 42,
  "users": [
    {
      "id": 11,
      "name": "Anna Kowalska",
      "email": "anna.kowalska@example.com",
      "role": "admin"
    },
    {
      "id": 12,
      "name": "Tomasz Nowak",
      "email": "tomasz.nowak@example.com",
      "role": "admin"
    }
  ]
}
