import pandas as pd
from scipy.io import arff

# data loading
try:
    data, meta = arff.loadarff('Rice_Cammeo_Osmancik.arff')
    df = pd.DataFrame(data)
    df['Class'] = df['Class'].str.decode('utf-8')
except FileNotFoundError:
    print("Error: 'Rice_Cammeo_Osmancik.arff' file not found.")
    exit()

# Convexity ratio (Convex_Area / Area)
df["Convexity"] = df["Convex_Area"] / df["Area"]

# Damage indicator (1 = damaged, 0 = normal)
df["Damaged"] = (df["Convexity"] < 0.95).astype(int)

print("Convexity summary:")
print(df["Convexity"].describe())

print("\nDamaged grains count:")
print(df["Damaged"].value_counts())