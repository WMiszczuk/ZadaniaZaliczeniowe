import json
import os

saldo = 0
magazyn = {}
historia = []


if os.path.exists("saldo.txt"):
    with open("saldo.txt", "r") as f:
        saldo = float(f.read())


if os.path.exists("magazyn.txt"):
    with open("magazyn.txt", "r") as f:
        magazyn = json.load(f)


if os.path.exists("historia.txt"):
    with open("historia.txt", "r") as f:
        historia = f.read().splitlines()


def menu():
    print("""
Dostępne komendy:
saldo
sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec
""")

menu()

while True:
    komenda = input("Podaj komendę: ").lower()

    # saldo
    if komenda == "saldo":
        try:
            kwota = float(input("Podaj kwotę do dodania / odjęcia: "))
            saldo += kwota
            historia.append(f"saldo {kwota}")
        except ValueError:
            print("Błędna kwota.")

    # zakup
    elif komenda == "zakup":
        try:
            nazwa = input("Nazwa produktu: ")
            cena = float(input("Cena produktu: "))
            ilosc = int(input("Liczba sztuk: "))

            if cena <= 0 or ilosc <= 0:
                print("Cena i ilość muszą być dodatnie.")
                continue

            koszt = cena * ilosc
            if saldo - koszt < 0:
                print("Brak środków na koncie.")
                continue

            saldo -= koszt

            if nazwa in magazyn:
                magazyn[nazwa]["ilosc"] += ilosc
                magazyn[nazwa]["cena"] = cena
            else:
                magazyn[nazwa] = {"cena": cena, "ilosc": ilosc}

            historia.append(f"zakup {nazwa} {cena} {ilosc}")

        except ValueError:
            print("Błędne dane.")

    # sprzedaż
    elif komenda == "sprzedaż":
        try:
            nazwa = input("Nazwa produktu: ")
            cena = float(input("Cena produktu: "))
            ilosc = int(input("Liczba sztuk: "))

            if nazwa not in magazyn:
                print("Brak produktu w magazynie.")
                continue

            if ilosc <= 0 or cena <= 0:
                print("Cena i ilość muszą być dodatnie.")
                continue

            if magazyn[nazwa]["ilosc"] < ilosc:
                print("Za mało sztuk w magazynie.")
                continue

            magazyn[nazwa]["ilosc"] -= ilosc
            saldo += cena * ilosc

            historia.append(f"sprzedaż {nazwa} {cena} {ilosc}")

        except ValueError:
            print("Błędne dane")


    elif komenda == "konto":
        print(f"Stan konta: {saldo} zł")


    elif komenda == "lista":
        if not magazyn:
            print("Magazyn jest pusty")
        else:
            for nazwa, dane in magazyn.items():
                print(f"{nazwa} | cena: {dane['cena']} | ilość: {dane['ilosc']}")


    elif komenda == "magazyn":
        nazwa = input("Podaj nazwę produktu: ")
        if nazwa in magazyn:
            dane = magazyn[nazwa]
            print(f"{nazwa} | cena: {dane['cena']} | ilość: {dane['ilosc']}")
        else:
            print("Brak produktu w magazynie.")


    elif komenda == "przegląd":
        if not historia:
            print("Brak zapisanych operacj")
            continue

        print(f"Liczba zapisanych komend: {len(historia)}")

        od = input("Od (puste = początek): ")
        do = input("Do (puste = koniec): ")

        try:
            start = int(od) if od else 0
            end = int(do) if do else len(historia)

            if start < 0 or end > len(historia):
                print("Zakres poza listą")
                continue

            for i in range(start, end):
                print(i, historia[i])

        except ValueError:
            print("Błędny zakres")

    elif komenda == "koniec":
 #zapisywanie

        with open("saldo.txt", "w") as f:
            f.write(str(saldo))


        with open("magazyn.txt", "w") as f:
            json.dump(magazyn, f)


        with open("historia.txt", "a") as f:
            for operacja in historia:
                f.write(operacja + "\n")

        print("Koniec programu")
        break
