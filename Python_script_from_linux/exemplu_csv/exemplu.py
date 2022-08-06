import csv

with open('lista.csv', 'r') as f:
    reader = csv.DictReader(f)
    items = list(reader)
    for item in items:
        print(item)