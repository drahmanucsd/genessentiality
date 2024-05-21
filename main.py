import pandas as pd

# Specify the relative path to the Excel file
file_path = "ecDNA Target genes.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
# Assuming the third column index is 2 (indexing starts from 0)
third_column = df.iloc[:, 2]


# Extract the text before the character "|"
extracted_text = third_column.str.split('|').str[0]
# Save the DataFrame to a CSV file
extracted_text.to_csv('extracted_text.csv', index=False)

# Create a new DataFrame with the extracted text


# Display the first few rows of the new DataFrame
print(extracted_text.head())