import pandas as pd

# Load the data
match_df = pd.read_csv('match.tsv', sep='\t', header=None)
depmap_df = pd.read_csv('DepMap-celllines.csv')

# Extract the second column of each DataFrame
match_cells = match_df.iloc[:, 1]
depmap_cells = depmap_df.iloc[:, 1]

# Create a new DataFrame to store matching rows
matched_rows = pd.DataFrame()

# Find matches
for cell in match_cells:
    matched_row = depmap_df[depmap_cells == cell]
    if not matched_row.empty:
        matched_rows = pd.concat([matched_rows, matched_row], ignore_index=True)

# Save the matched rows to a new CSV file (optional)
matched_ids = matched_rows.iloc[:,:1]
concatenated_df = pd.concat([match_df, matched_ids], axis=1)
headers = ['Gene Id', 'Cell Line',"ecDNA Content","DP Cell Line ID"]
concatenated_df.columns = headers
matched_ids.to_csv('matched_ids.csv', index=False)
concatenated_df.to_csv('match.csv', index=False )

print("Matching rows have been saved to 'matched_rows.csv'")
print(concatenated_df['DP Cell Line ID'])
#concatenated_df['DP Cell Line ID'].to_csv('DP_cell_line_ID.csv', sep = ',')