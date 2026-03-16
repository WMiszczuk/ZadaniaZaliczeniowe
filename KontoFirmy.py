import json
import os


class Manager:

    def __init__(self):
        self.saldo = 0
        self.magazyn = {}
        self.historia = []
        self.actions = {}

        self.load_data()

    def assign(self, name, func):
        self.actions[name] = func


    def execute(self, name):
        if name in self.actions:
            self.actions[name]()
        else:
            print("Nieznana komenda")

    # wczytywanie

    def load_data(self):

        if os.path.exists("saldo.txt"):
            with open("saldo.txt") as f:
                self.saldo = float(f.read())

        if os.path.exists("magazyn.txt"):
            with open("magazyn.txt") as f:
                self.magazyn = json.load(f)

        if os.path.exists("historia.txt"):
            with open("historia.txt") as f:
                self.historia = f.read().splitlines()

    # zapis
    def save_data(self):

        with open("saldo.txt", "w") as f:
            f.write(str(self.saldo))

        with open("magazyn.txt", "w") as f:
            json.dump(self.magazyn, f)

        with open("historia.txt", "w") as f:
            for operacja in self.historia:
                f.write(operacja + "\n")

    def menu(self):
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

    # kom3ndy

    def saldo_cmd(self):
        try:
            kwota = float(input("Podaj kwotę: "))
            self.saldo += kwota
            self.historia.append(f"saldo {kwota}")
        except ValueError:
            print("Błędna kwota")

    def zakup_cmd(self):

        try:
            nazwa = input("Nazwa produktu: ")
            cena = float(input("Cena: "))
            ilosc = int(input("Ilość: "))

            if cena <= 0 or ilosc <= 0:
                print("Cena i ilość muszą być dodatnie")
                return

            koszt = cena * ilosc

            if self.saldo - koszt < 0:
                print("Brak środków")
                return

            self.saldo -= koszt

            if nazwa in self.magazyn:
                self.magazyn[nazwa]["ilosc"] += ilosc
                self.magazyn[nazwa]["cena"] = cena
            else:
                self.magazyn[nazwa] = {"cena": cena, "ilosc": ilosc}

            self.historia.append(f"zakup {nazwa} {cena} {ilosc}")

        except ValueError:
            print("Błędne dane")

    def sprzedaz_cmd(self):

        try:
            nazwa = input("Nazwa produktu: ")
            cena = float(input("Cena: "))
            ilosc = int(input("Ilość: "))

            if nazwa not in self.magazyn:
                print("Brak produktu")
                return

            if self.magazyn[nazwa]["ilosc"] < ilosc:
                print("Za mało w magazynie")
                return

            self.magazyn[nazwa]["ilosc"] -= ilosc
            self.saldo += cena * ilosc

            self.historia.append(f"sprzedaż {nazwa} {cena} {ilosc}")

        except ValueError:
            print("Błędne dane")

    def konto_cmd(self):
        print(f"Stan konta: {self.saldo}")

    def lista_cmd(self):

        if not self.magazyn:
            print("Magazyn pusty")
            return

        for nazwa, dane in self.magazyn.items():
            print(nazwa, dane)

    def magazyn_cmd(self):

        nazwa = input("Produkt: ")

        if nazwa in self.magazyn:
            print(self.magazyn[nazwa])
        else:
            print("Brak produktu")

    def przeglad_cmd(self):

        if not self.historia:
            print("Brak historii")
            return

        print("Liczba komend:", len(self.historia))

        od = input("Od: ")
        do = input("Do: ")

        start = int(od) if od else 0
        end = int(do) if do else len(self.historia)

        if start < 0 or end > len(self.historia):
            print("Zakres poza listą")
            print("Liczba zapisanych komend:", len(self.historia))
            return

        for i in range(start, end):
            print(i, self.historia[i])

    def koniec_cmd(self):

        self.save_data()
        print("Koniec programu")
        exit()


manager = Manager()

manager.assign("saldo", manager.saldo_cmd)
manager.assign("zakup", manager.zakup_cmd)
manager.assign("sprzedaż", manager.sprzedaz_cmd)
manager.assign("konto", manager.konto_cmd)
manager.assign("lista", manager.lista_cmd)
manager.assign("magazyn", manager.magazyn_cmd)
manager.assign("przegląd", manager.przeglad_cmd)
manager.assign("koniec", manager.koniec_cmd)

while True:
    manager.menu()
    komenda = input("Podaj komendę: ").lower()
    manager.execute(komenda)