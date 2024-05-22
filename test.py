import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv'
df = pd.read_csv(file_path)

# Check the first few rows of the DataFrame to understand its structure
print(df.head())

# Extract the values for the gene "RAE1"
rae1_values = df['RAE1']

# Calculate the average of these values
average_rae1 = rae1_values.mean()

print(f"The average of the values for the gene 'RAE1' is: {average_rae1}")
