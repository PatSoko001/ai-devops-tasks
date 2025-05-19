Zadanie 12: Usprawnienie kodu

Oryginalny kod
python
Copy
Edit
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates


Usprawnienie kodu
Oryginalny kod ma złożoność czasową O(n²), ponieważ dla każdej pary elementów w liście porównuje je, co może prowadzić do dużej liczby operacji przy dużych zbiorach danych.

Optymalną metodą rozwiązania tego problemu jest użycie struktury danych, która pozwala na szybkie sprawdzanie, czy dany element już wystąpił. Jednym z takich rozwiązań jest użycie zestawu (set) do śledzenia elementów, które już zostały napotkane.


Zoptymalizowana wersja
python
Copy
Edit
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()
    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)



Wyjaśnienie usprawnień
Zmiana na zestawy (set):
Zestawy umożliwiają szybkie sprawdzanie, czy element już wystąpił (operacja w czasie O(1) na średnio). Dzięki temu, zamiast przeszukiwać całą listę dla każdego elementu, przechowujemy napotkane elementy w zestawie i sprawdzamy je na bieżąco.

Redukcja złożoności czasowej:
Nowa wersja funkcji ma złożoność O(n), ponieważ przechodzimy po liście tylko raz, a operacje wstawiania i sprawdzania elementów w zestawie są średnio wykonywane w czasie stałym.

Wykorzystanie zestawu do przechowywania duplikatów:
Użycie zestawu (set) do przechowywania duplikatów zamiast listy pozwala na automatyczne uniknięcie duplikujących się elementów, ponieważ zestawy nie dopuszczają powtarzania elementów.

Zwracanie listy:
Na końcu przekształcamy zestaw duplicates z powrotem na listę, aby zachować spójność z oryginalną funkcją.




Podsumowanie
Oryginalny kod miał złożoność O(n²) z powodu zagnieżdżonych pętli, które porównywały każdą parę elementów w liście.

Zoptymalizowana wersja używa zestawu, co pozwala na osiągnięcie złożoności O(n), co jest znacznie bardziej wydajne przy dużych zbiorach danych.
