import pandas as pd

print("Reading the first 5 rows of the dataset...")

df = pd.read_csv("DATA.csv", nrows=5)

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.to_string(index=False))

print("\nDataset inspection completed!")