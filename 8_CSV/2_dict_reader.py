import csv

with open("sample_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['name']} is a {row['age']}-year-old {row['role']} from {row['city']}.")