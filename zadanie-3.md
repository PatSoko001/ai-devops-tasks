 Zadanie 3: Podstawowe formatowanie promptu

## Prompt 1: Niestrukturyzowany

**Użyty prompt:**
dockerfile node

sql
Copy
Edit

**Wygenerowana odpowiedź:**  Dockerfile

FROM node:latest

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
Prompt 2: Strukturyzowany
Użyty prompt:

diff
Copy
Edit
Napisz prosty Dockerfile dla aplikacji Node.js, który:
- używa Node 18 jako obrazu bazowego
- kopiuje pliki package.json i package-lock.json
- instaluje zależności
- kopiuje resztę plików aplikacji
- wystawia port 3000
- uruchamia aplikację poleceniem "npm start"
Wygenerowana odpowiedź:

Dockerfile
Copy
Edit
FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
