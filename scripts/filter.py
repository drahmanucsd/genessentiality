import pandas as pd

# Specify the relative paths to the input files
gene_list = "../Initial datasets/ecDNA Target genes.xlsx"
raw_data = "../Initial datasets/aggregated_results.csv"
depmap_file = '../DepMap-celllines.csv'

# Read the Excel file into a DataFrame
gene_list_df = pd.read_excel(gene_list)
raw_data_df = pd.read_csv(raw_data)
depmap_df = pd.read_csv(depmap_file)

# Extract the relevant columns
gene_column = gene_list_df.iloc[:, 2]
sample_col = raw_data_df.iloc[:, 1]
class_col = raw_data_df.iloc[:, 4]
gene_col = raw_data_df.iloc[:, 22]

# Extract the text before the character "|" which contains the gene name
gene_name = gene_column.str.split('|').str[0].tolist()

# Create a DataFrame to store the match data
match_data = []

# Populate the match data
for i in range(len(gene_name)):
    for j in range(len(sample_col)):
        if gene_name[i] in gene_col[j]:
            ecDNA_content = "pos" if class_col[j] == "ecDNA" else "neg"
            match_data.append([gene_name[i], sample_col[j], ecDNA_content])

# Convert match data to a DataFrame
match_df = pd.DataFrame(match_data, columns=['Gene Id', 'Cell Line', 'ecDNA Content'])

# Extract the second column of each DataFrame
match_cells = match_df['Cell Line']
depmap_cells = depmap_df.iloc[:, 1]

# Create a new DataFrame to store matching rows
matched_rows = pd.DataFrame()

# Find matches
for cell in match_cells:
    matched_row = depmap_df[depmap_cells == cell]
    if not matched_row.empty:
        matched_rows = pd.concat([matched_rows, matched_row], ignore_index=True)

# Extract matched IDs
matched_ids = matched_rows.iloc[:, :1]

# Concatenate match_df with matched_ids
concatenated_df = pd.concat([match_df, matched_ids], axis=1)

# Define headers
headers = ['Gene Id', 'Cell Line', 'ecDNA Content', 'DP Cell Line ID']
concatenated_df.columns = headers

# Save the results to CSV files (optional)
matched_ids.to_csv('../output files/matched_ids.csv', index=False)
concatenated_df.to_csv('../output files/match.csv', index=False)

# Print the resulting DataFrame
print("Matching rows have been saved to 'matched_ids.csv' and 'match.csv'")
print(concatenated_df['DP Cell Line ID'])

# Optional: Save DP Cell Line IDs to a separate file
# concatenated_df['DP Cell Line ID'].to_csv('DP_cell_line_ID.csv', sep=',')
