 Test jednostkowy przy użyciu Jest
1. Co to jest Jest?
Jest to popularne narzędzie do testowania aplikacji JavaScript, stworzone przez Facebooka. Jest szybkie, ma wbudowaną obsługę asercji, umożliwia testowanie kodu synchronicznego i asynchronicznego, a także zawiera mechanizmy do mockowania i szpiegowania funkcji. Jest to framework używany głównie do testowania aplikacji React, ale może być stosowany do dowolnych projektów JavaScript.

Uruchamianie testów
Po zainstalowaniu Jest i utworzeniu plików, możemy uruchomić testy. Aby to zrobić, należy dodać skrypt w pliku package.json:

json
Copy
Edit
"scripts": {
  "test": "jest"
}
Następnie uruchamiamy testy za pomocą polecenia:

bash
Copy
Edit
npm test
Jest automatycznie wykryje pliki testowe i wykona je, a wyniki testów zostaną wyświetlone w konsoli.




Struktura plików projektu
Po utworzeniu funkcji i testu, struktura plików projektu powinna wyglądać tak:

go
Copy
Edit
/projekt
  ├── sum.js           // Plik z funkcją sum
  ├── sum.test.js      // Plik z testami jednostkowymi
  ├── package.json     // Plik konfiguracyjny projektu z zależnością do Jest



Podsumowanie
Jest to narzędzie do testowania JavaScript, które umożliwia pisanie testów jednostkowych.

W sum.js zapisaliśmy funkcję, która dodaje dwie liczby.

W sum.test.js stworzyliśmy testy, które sprawdzają poprawność tej funkcji.

Aby uruchomić testy, należy zainstalować Jest, dodać odpowiedni skrypt w package.json i uruchomić testy za pomocą npm test.
