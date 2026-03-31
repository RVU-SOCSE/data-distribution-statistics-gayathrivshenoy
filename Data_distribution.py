import pandas as pd

# Load the dataset
df = pd.read_csv('1experience.csv')

# Display first few rows
print("Dataset Preview:")
print(df.head())

# Assuming the column name is 'Experience'
# (change if your column name is different)
col = 'Experience'

# --- Central Tendencies ---
mean_val = df[col].mean()
median_val = df[col].median()
mode_val = df[col].mode()[0]

print("\n--- Central Tendency Measures ---")
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")

# --- Dispersion Measures ---
min_val = df[col].min()
max_val = df[col].max()
range_val = max_val - min_val
variance_val = df[col].var()
std_dev_val = df[col].std()

print("\n--- Dispersion Measures ---")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Range: {range_val}")
print(f"Variance: {variance_val}")
print(f"Standard Deviation: {std_dev_val}")

# --- Distribution Analysis ---
print("\n--- Distribution Analysis ---")

if mean_val > median_val:
    print("Distribution is positively skewed (right-skewed).")
elif mean_val < median_val:
    print("Distribution is negatively skewed (left-skewed).")
else:
    print("Distribution is approximately symmetric.")

# Optional: describe full statistics
print("\n--- Summary Statistics ---")
print(df[col].describe())
