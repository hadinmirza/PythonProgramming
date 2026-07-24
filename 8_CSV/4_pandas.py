import pandas as pd

df = pd.read_csv("sample_data.csv")

print(df.head())
print()
print("Average Age:", df["age"].mean())