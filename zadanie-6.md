Zadanie 6: Pierwszy diagram Mermaid

## 🔹 Prompt użyty do wygenerowania kodu

Stwórz prosty diagram Mermaid pokazujący proces CI/CD: commit → build → test → deploy.

css
Copy
Edit

## 🔹 Wygenerowany kod Mermaid

mermaid
graph TD
    A[Commit] --> B[Build]
    B --> C[Test]
    C --> D[Deploy]
🔹 Opis wygenerowanego diagramu
Diagram składa się z czterech kroków ułożonych liniowo w kierunku od lewej do prawej (lub od góry do dołu, zależnie od widoku):

Commit – pierwszy krok, inicjujący proces (np. push do repozytorium)

Build – krok kompilacji/konstrukcji aplikacji

Test – krok testów automatycznych

Deploy – końcowy etap wdrożenia na środowisko docelowe

Strzałki pokazują kolejność przepływu operacji: Commit → Build → Test → Deploy

🔹 Podgląd diagramu
Diagram został zwizualizowany w Mermaid Live Editor, a jego wygląd to klasyczny liniowy flowchart ze strzałkami kierunkowymi pomiędzy prostokątnymi węzłami.
