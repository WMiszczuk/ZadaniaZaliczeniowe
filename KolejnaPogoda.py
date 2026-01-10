import requests
import json
import os
from datetime import datetime, timedelta



class WeatherForecast:
    def __init__(self, latitude, longitude, filename="wyniki.json"):
        self.latitude = latitude
        self.longitude = longitude
        self.filename = filename
        self.data = {}

        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.data = json.load(f)



    # zapis do pliku
    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    # getitem
    def __getitem__(self, date):
        if date in self.data:
            return self.data[date]

        wynik = self._fetch_from_api(date)
        self.data[date] = wynik
        self.save()
        return wynik


    # setitem
    def __setitem__(self, date, value):
        self.data[date] = value
        self.save()

    # iter
    def __iter__(self):
        return iter(self.data.keys())

    # items
    def items(self):
        for k, v in self.data.items():
            yield (k, v) #po kolei

    # api
    def _fetch_from_api(self, date):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            f"&daily=rain_sum"
            f"&timezone=Europe%2FLondon"
            f"&start_date={date}"
            f"&end_date={date}"
        )


        try:
            response = requests.get(url)
            response.raise_for_status()
            dane = response.json()
            rain = dane["daily"]["rain_sum"][0]

            if rain > 0:
                return "Będzie padać"
            elif rain == 0:
                return "Nie będzie padać"
            else:
                return "Nie wiem"

        except Exception:
            return "Nie wiem"



# program

weather_forecast = WeatherForecast(52.23, 21.01)

date = input("Podaj datę (YYYY-MM-DD), jeśli chcesz sprawdzić jutrzejszą pogodę, klinkij Enter: ")

if date == "":
    date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")


print(weather_forecast[date])


# weather_forecast[date]
# weather_forecast.items()
# weather_forecast jako iterator

