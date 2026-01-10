import requests
import json
import os
from datetime import datetime, timedelta

# ustawienia
LATITUDE = 52.23     # Warszawa
LONGITUDE = 21.01
PLIK = "wyniki.json"

# wczytywanie
if os.path.exists(PLIK):
    with open(PLIK, "r", encoding="utf-8") as f:
        zapisane = json.load(f)
else:
    zapisane = {}

# data
data = input("Podaj datę (YYYY-MM-DD) lub Enter = jutro: ")

if data == "":
    data = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# jesli jest w pliku
if data in zapisane:
    print(zapisane[data])
    exit()

# zapytanie api
url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LATITUDE}"
    f"&longitude={LONGITUDE}"
    f"&daily=rain_sum"
    f"&timezone=Europe%2FLondon"
    f"&start_date={data}"
    f"&end_date={data}"
)

response = requests.get(url)

if response.status_code != 200:
    wynik = "Nie wiem"
else:
    dane = response.json()

    try:
        rain = dane["daily"]["rain_sum"][0]

        if rain > 0:
            wynik = "Będzie padać"
        elif rain == 0:
            wynik = "Nie będzie padać"
        else:
            wynik = "Nie wiem"
    except:
        wynik = "Nie wiem"

# zapis
zapisane[data] = wynik

with open(PLIK, "w", encoding="utf-8") as f:
    json.dump(zapisane, f, indent=2, ensure_ascii=False)


print(wynik)
