import sys

# sprawdzanie argumentów
if len(sys.argv) < 3:
    print("Użycie: python reader.py in.csv out.csv zmiana1 zmiana2 ...")
    sys.exit(1)

plik_wejsciowy = sys.argv[1]
plik_wyjsciowy = sys.argv[2]
zmiany = sys.argv[3:]

# odczyt csv
with open(plik_wejsciowy, "r", encoding="utf-8") as f:
    dane = []
    for linia in f:
        dane.append(linia.strip().split(","))

# modyfikacje
for zmiana in zmiany:
    x, y, wartosc = zmiana.split(",")

    x = int(x)
    y = int(y)

    if y < len(dane) and x < len(dane[y]):
        dane[y][x] = wartosc
    else:
        print(f"Nieprawidłowe współrzędne: {zmiana}")

# terminal - wyświetlanie
print("\nZawartość po zmianach:")
for wiersz in dane:
    print(",".join(wiersz))

# zapis do pliku
with open(plik_wyjsciowy, "w", encoding="utf-8") as f:
    for wiersz in dane:
        f.write(",".join(wiersz) + "\n")
