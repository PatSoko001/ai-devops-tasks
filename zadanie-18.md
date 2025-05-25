Zadanie 18: Analiza wymagań bezpieczeństwa

5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym

1. **Używaj minimalnych, zaufanych obrazów bazowych**  
   Minimalizuje powierzchnię ataku i zmniejsza ryzyko podatności.

2. **Uruchamiaj kontenery jako nieuprzywilejowany użytkownik**  
   Dzięki temu w przypadku włamania atakujący ma ograniczone możliwości.

3. **Ogranicz dostęp do zasobów (CPU, pamięć, sieć)**  
   Zapobiega nadużyciom zasobów przez nieautoryzowany kod.

4. **Regularnie skanuj obrazy pod kątem podatności**  
   Automatyczne skanowanie pomaga wcześnie wykrywać problemy.

5. **Używaj mechanizmu `read-only` i `tmpfs` dla kontenerów**  
   Ogranicza możliwość zapisu i modyfikacji systemu plików.




**Jak mogę zaimplementować pierwszą z tych praktyk w moim Dockerfile i docker-compose.yml?**

Odpowiedź:

Aby zaimplementować **minimalne, zaufane obrazy bazowe**, wybieraj obrazy typu `alpine`, `distroless` lub obrazy oficjalne o ograniczonej zawartości.


Przykład implementacji:

#### Dockerfile

Zamiast używać np. `node:latest`, użyj:

```dockerfile
FROM node:20-alpine

# Ustaw katalog roboczy
WORKDIR /app

# Kopiuj pliki
COPY package*.json ./
RUN npm install --production

COPY . .

# Ustaw użytkownika nieuprzywilejowanego (praktyka 2 przy okazji)
RUN addgroup app && adduser -S -G app app
USER app

CMD ["node", "app.js"]
