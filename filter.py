import pandas as pd

# Specify the relative path to the Excel file
file_path = "ecDNA Target genes.xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Assuming the third column index is 2 (indexing starts from 0)
third_column = df.iloc[:, 2]

# Extract the text before the character "|"
extracted_text = third_column.str.split('|').str[0]

# Convert the Series to a single string with space-separated values
extracted_text_str = ' '.join(extracted_text.dropna().astype(str))

# Save the string to a text file
with open('extracted_text.txt', 'w') as f:
    f.write(extracted_text_str)

print("Genes extracted successfully.")
