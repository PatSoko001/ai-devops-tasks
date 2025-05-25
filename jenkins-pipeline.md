```mermaid
graph TD
    A[Checkout kodu z repozytorium] --> B[Budowanie aplikacji]
    B --> C[Testy jednostkowe]
    C --> D[Analiza statyczna kodu]
    D --> E[Skany bezpieczeństwa]
    E --> F[Budowanie obrazu Docker]
    F --> G[Testy integracyjne]
    G --> H[Wdrożenie na środowisko staging]
    H --> I{Manualna akceptacja}
    I -->|Tak| J[Wdrożenie na produkcję]
    I -->|Nie| K[Zatrzymanie procesu]
