import csv

with open("sample_data.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)