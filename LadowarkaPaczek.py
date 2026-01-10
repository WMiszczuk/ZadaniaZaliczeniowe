liczba_paczek = int(input('Ile elementów chcesz wysłać?: '))

limit = 20
aktualna_paczka = []
paczki = []

for i in range(liczba_paczek):
    waga = int(input('Ile waży element?: '))

    # warunek zakończenia
    if waga < 1 or waga > 10:
        break

    if sum(aktualna_paczka) + waga <= limit:
        aktualna_paczka.append(waga)
    else:
        paczki.append(aktualna_paczka)
        aktualna_paczka = [waga]

# dodanie ostatniej paczki
if aktualna_paczka:
    paczki.append(aktualna_paczka)

# podsumowanie
wyslane_paczki = len(paczki)
laczna_waga = sum(sum(p) for p in paczki)

puste_kilogramy = []
for paczka in paczki:
    puste_kilogramy.append(limit - sum(paczka))

suma_pustych = sum(puste_kilogramy)
max_puste = max(puste_kilogramy)
nr_paczki = puste_kilogramy.index(max_puste) + 1

print('\nPodsumowanie:')
print(f'Wysłano {wyslane_paczki} paczek: ')
print(f'Wysłano {laczna_waga} kg')
print(f'Suma pustych kilogramów: {suma_pustych} kg')
print(f'Najwięcej pustych kilogramów ma paczka {nr_paczki} ({max_puste} kg)')
