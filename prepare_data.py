import pandas as pd
import os

INPUT_FILE = "DATA.csv"
OUTPUT_FILE = "data_sample.csv"

CHUNK_SIZE = 100000
NORMAL_SAMPLE_FRAC = 0.02

print("Preparing the dataset...")

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

first_chunk = True
total_rows = 0
total_fraud = 0

for chunk in pd.read_csv(INPUT_FILE, chunksize=CHUNK_SIZE):

    fraud = chunk[chunk["isFraud"] == 1]

    normal = chunk[chunk["isFraud"] == 0].sample(
        frac=NORMAL_SAMPLE_FRAC,
        random_state=42
    )

    sample = pd.concat([fraud, normal])

    sample.to_csv(
        OUTPUT_FILE,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    first_chunk = False
    total_rows += len(sample)
    total_fraud += len(fraud)

    print("Rows prepared:", total_rows)

print("\nDataset preparation completed!")
print("Total sampled rows:", total_rows)
print("Fraud transactions:", total_fraud)
print("Saved file:", OUTPUT_FILE)