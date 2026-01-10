# DANE
uczniowie = []       # {"imie": "", "nazwisko": "", "klasa": ""}
nauczyciele = []      # {"imie": "", "nazwisko": "", "przedmiot": "", "klasy": []}
wychowawcy = []      # {"imie": "", "nazwisko": "", "klasa": ""}

# menu
while True:
    print("\nKomendy: utwórz, zarządzaj, koniec")
    komenda = input(">> ").lower()

    # utwórz
    if komenda == "utwórz":
        while True:
            print("\nOpcje: uczeń, nauczyciel, wychowawca, koniec")
            opcja = input(">>> ").lower()

            # UCZEŃ
            if opcja == "uczeń":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")
                klasa = input("Klasa: ")
                uczniowie.append({
                    "imie": imie,
                    "nazwisko": nazwisko,
                    "klasa": klasa
                })

            # NAUCZYCIEL
            elif opcja == "nauczyciel":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")
                przedmiot = input("Przedmiot: ")

                klasy = []
                print("Podaj klasy (pusta linia kończy):")
                while True:
                    k = input()
                    if k == "":
                        break
                    klasy.append(k)

                nauczyciele.append({
                    "imie": imie,
                    "nazwisko": nazwisko,
                    "przedmiot": przedmiot,
                    "klasy": klasy
                })

            # WYCHOWAWCA
            elif opcja == "wychowawca":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")
                klasa = input("Prowadzona klasa: ")

                wychowawcy.append({
                    "imie": imie,
                    "nazwisko": nazwisko,
                    "klasa": klasa
                })

            elif opcja == "koniec":
                break

            else:
                print("Nieznana opcja.")

    # zarządzaj
    elif komenda == "zarządzaj":
        while True:
            print("\nOpcje: klasa, uczen, nauczyciel, wychowawca, koniec")
            opcja = input(">>> ").lower()

            # KLASA
            if opcja == "klasa":
                klasa = input("Podaj klasę: ")

                print("\nUczniowie:")
                for u in uczniowie:
                    if u["klasa"] == klasa:
                        print(u["imie"], u["nazwisko"])

                print("Wychowawca:")
                for w in wychowawcy:
                    if w["klasa"] == klasa:
                        print(w["imie"], w["nazwisko"])

            # UCZEŃ
            elif opcja == "uczen":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")

                klasa_ucznia = None
                for u in uczniowie:
                    if u["imie"] == imie and u["nazwisko"] == nazwisko:
                        klasa_ucznia = u["klasa"]

                if not klasa_ucznia:
                    print("Nie znaleziono ucznia")
                    continue

                print("\nLekcje:")
                for n in nauczyciele:
                    if klasa_ucznia in n["klasy"]:
                        print(n["przedmiot"], "-", n["imie"], n["nazwisko"])

            # NAUCZYCIEL
            elif opcja == "nauczyciel":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")

                for n in nauczyciele:
                    if n["imie"] == imie and n["nazwisko"] == nazwisko:
                        print("Prowadzi klasy:", ", ".join(n["klasy"]))

            # WYCHOWAWCA
            elif opcja == "wychowawca":
                imie = input("Imię: ")
                nazwisko = input("Nazwisko: ")

                klasa = None
                for w in wychowawcy:
                    if w["imie"] == imie and w["nazwisko"] == nazwisko:
                        klasa = w["klasa"]

                if not klasa:
                    print("Nie znaleziono wychowawcy")
                    continue

                print("\nUczniowie klasy", klasa)
                for u in uczniowie:
                    if u["klasa"] == klasa:
                        print(u["imie"], u["nazwisko"])

            elif opcja == "koniec":
                break

            else:
                print("Nieznaa opcja.")

#koniec
    elif komenda == "koniec":
        print("Zakończono program")
        break

    else:
        print("Nieznana komenda.")
