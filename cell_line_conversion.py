import pandas as pd

# Load the data
match_df = pd.read_csv('match.tsv', sep='\t', header=None)
depmap_df = pd.read_csv('DepMap-2018q3-celllines.csv')

# Extract the second column of each DataFrame
match_cells = match_df.iloc[:, 1]
depmap_cells = depmap_df.iloc[:, 1]

# Create a new DataFrame to store matching rows
matched_rows = pd.DataFrame()

# Function to generate prefixes of length greater than 3
def generate_prefixes(cell):
    return [cell[:i] for i in range(4, len(cell)+1)]

# Find matches
for cell in match_cells:
    prefixes = generate_prefixes(cell)
    for prefix in prefixes:
        matched_row = depmap_df[depmap_cells.str.contains(prefix, na=False)]
        if not matched_row.empty:
            matched_rows = pd.concat([matched_rows, matched_row], ignore_index=True)

# Drop duplicates in case of multiple matches
matched_rows = matched_rows.drop_duplicates()

# Extract the first column of matched_rows
match_ids = matched_rows.iloc[:, 0]

# Save the matched rows to a new CSV file (optional)
match_ids.to_csv('matched_ids.csv', index=False)

print("Matching rows have been saved to 'matched_rows.csv'")
print("Match IDs:", match_ids.tolist())
