import sys
import json
import pickle
import os


# klasa bazowa!!
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read(self):
        raise NotImplementedError

    def write(self, filename):
        raise NotImplementedError

    def modify(self, x, y, value):
        if y < len(self.data) and x < len(self.data[y]):
            self.data[y][x] = value
        else:
            print(f"Błędne współrzędne: {x},{y}")

    def display(self):
        for row in self.data:
            print(",".join(map(str, row)))


# CSV
class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = [line.strip().split(",") for line in f]

    def write(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for row in self.data:
                f.write(",".join(map(str, row)) + "\n")


# JSON
class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def write(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f)



# TXT
class TXTHandler(FileHandler):
    def read(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = [line.strip().split(",") for line in f]

    def write(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for row in self.data:
                f.write(",".join(map(str, row)) + "\n")


# PICKLE
class PickleHandler(FileHandler):
    def read(self):
        with open(self.filename, "rb") as f:
            self.data = pickle.load(f)

    def write(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.data, f)


# FABRYKA
def get_handler(filename):
    if filename.endswith(".csv"):
        return CSVHandler(filename)
    if filename.endswith(".json"):
        return JSONHandler(filename)
    if filename.endswith(".txt"):
        return TXTHandler(filename)
    if filename.endswith(".pickle"):
        return PickleHandler(filename)
    raise ValueError("Nieobsługiwany format pliku")


# główny
if len(sys.argv) < 3:
    print("Użycie: python reader.py in.xxx out.xxx zmiana1 zmiana2 ...")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]

handler = get_handler(input_file)
handler.read()

for change in changes:
    x, y, value = change.split(",")
    handler.modify(int(x), int(y), value)

print("\nZawartość po zmianach:")
handler.display()



output_handler = get_handler(output_file)
output_handler.data = handler.data
output_handler.write(output_file)
