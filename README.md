# Gra_w_zgadywanie_liczb_01

Warsztat_1/Zadanie_1

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:

* Zadać pytanie: `Guess the number: ` i pobrać liczbę z klawiatury.
* Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat `It's not a number!`, 
po czym wrócić do pkt. 1 
* Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat `Too small!`, 
po czym wrócić do pkt. 1. 
* Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat `Too big!`, 
po czym wrócić do pkt. 1. 
* Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat `You win!`, 
po czym zakończyć działanie programu.

Przykład:
```python
Guess the number: cześć
It's not a number!
Guess the number: 50
Too small!
Guess the number: 75
Too big!
Guess the number: 63
You win!
```
Pamiętaj, aby obsłużyć odpowiednie błędy!
