Zadanie 17: Implementacja funkcji zgodnej z wymaganiami

## Opis funkcjonalności

Stworzona funkcja getCompletedTaskTitles:

- przyjmuje tablicę zadań w postaci obiektów ({ id, title, status }),
- filtruje tylko te, które mają status "completed",
- sortuje je według id w kolejności rosnącej,
- zwraca **tablicę tytułów** (title) tych ukończonych zadań.

Funkcja została zaimplementowana w języku JavaScript i może być używana w projektach Node.js lub aplikacjach webowych.

---

## Przykład użycia

javascript
const { getCompletedTaskTitles } = require('./task-filter');

const tasks = [
  { id: 3, title: "Zadanie C", status: "completed" },
  { id: 1, title: "Zadanie A", status: "in progress" },
  { id: 2, title: "Zadanie B", status: "completed" },
  { id: 4, title: "Zadanie D", status: "pending" }
];

const result = getCompletedTaskTitles(tasks);
console.log(result); // ["Zadanie B", "Zadanie C"]
