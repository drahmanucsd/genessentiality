import pandas as pd

# Specify the relative path to the Excel file
file_path = "ecDNA Target genes.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())
