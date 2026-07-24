import csv

engineers = 0
total_age = 0
people = 0

with open("sample_data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        people += 1
        total_age += int(row["age"])

        if row["role"] == "Engineer":
            engineers += 1

print(f"Number of Engineers: {engineers}")
print(f"Average Age: {total_age / people:.2f}")