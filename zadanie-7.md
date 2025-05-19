Zadanie 7: Skrypt do sprawdzania stanu usługi Docker

## Prompt użyty do wygenerowania skryptu

**Użyty prompt:**
Napisz prosty skrypt bash, który sprawdza, czy usługa Docker działa, a jeśli nie - próbuje ją uruchomić.

bash
Copy
Edit

##  Wygenerowany skrypt

bash
#!/bin/bash

# Sprawdzenie, czy usługa Docker działa
if systemctl is-active --quiet docker; then
    echo "Usługa Docker działa."
else
    echo "Usługa Docker nie działa. Próba uruchomienia..."
    # Próba uruchomienia usługi Docker
    sudo systemctl start docker
    if systemctl is-active --quiet docker; then
        echo "Usługa Docker została pomyślnie uruchomiona."
    else
        echo "Nie udało się uruchomić usługi Docker."
    fi
fi
🔹 Wyjaśnienie działania skryptu
1. #!/bin/bash
To jest tzw. "shebang", który mówi systemowi operacyjnemu, że skrypt ma być uruchomiony za pomocą interpretera bash.

2. if systemctl is-active --quiet docker; then
Ta linia sprawdza, czy usługa Docker działa. Komenda systemctl is-active sprawdza status usługi (czy jest aktywna). Flaga --quiet sprawia, że wynik nie jest wyświetlany na ekranie (chcemy tylko status, nie interesują nas dodatkowe informacje).

3. echo "Usługa Docker działa."
Jeśli usługa Docker działa, na ekranie wyświetli się komunikat "Usługa Docker działa."

4. else
Jeśli usługa Docker nie jest aktywna, program przechodzi do części else, aby podjąć próbę uruchomienia usługi.

5. echo "Usługa Docker nie działa. Próba uruchomienia..."
Wyświetla komunikat informujący, że usługa Docker nie działa i rozpoczyna się próba jej uruchomienia.

6. sudo systemctl start docker
Komenda sudo systemctl start docker uruchamia usługę Docker. Potrzebujemy uprawnień administratora (stąd użycie sudo), aby wykonać tę operację.

7. if systemctl is-active --quiet docker; then
Po próbie uruchomienia usługi Docker ponownie sprawdzamy, czy usługa jest aktywna.

8. echo "Usługa Docker została pomyślnie uruchomiona."
Jeśli usługa Docker została pomyślnie uruchomiona, na ekranie pojawi się komunikat "Usługa Docker została pomyślnie uruchomiona."

9. else
Jeśli po próbie uruchomienia usługi Docker nadal nie jest aktywna, przechodzimy do sekcji else, która wyświetli komunikat o nieudanej próbie uruchomienia.

10. echo "Nie udało się uruchomić usługi Docker."
Wyświetla komunikat, że uruchomienie usługi Docker nie powiodło się.

 Podsumowanie
Ten skrypt bash sprawdza, czy usługa Docker jest uruchomiona, a jeśli nie – stara się ją uruchomić. Jeśli usługa Docker jest już aktywna, skrypt po prostu informuje użytkownika, że działa. W przeciwnym razie próbuje uruchomić usługę i informuje o wyniku próby.
