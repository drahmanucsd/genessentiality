import pandas as pd

# Load the data
match_df = pd.read_csv('match.tsv', sep='\t', header=None)
depmap_df = pd.read_csv('DepMap-2018q3-celllines.csv')

# Extract the second column of each DataFrame
match_cells = match_df.iloc[:, 1]
depmap_cells = depmap_df.iloc[:, 1]

# Create a new DataFrame to store matching rows
matched_ids = pd.DataFrame(columns=['DepMap_ID', 'Match_ID'])

# Function to generate prefixes of length greater than 3
def generate_prefixes(cell):
    return [cell[:i] for i in range(4, len(cell)+1)]

# Find matches
for match_id, cell in zip(match_df.iloc[:, 1], match_cells):  # Iterate over the second column of match.tsv
    prefixes = generate_prefixes(cell)
    for prefix in prefixes:
        matched_row = depmap_df[depmap_cells.str.contains(prefix, na=False)]
        if not matched_row.empty:
            matched_ids = pd.concat([matched_ids, pd.DataFrame({'DepMap_ID': matched_row.iloc[:, 0], 'Match_ID': [match_id] * len(matched_row)})], ignore_index=True)

# Drop duplicates in case of multiple matches
matched_ids = matched_ids.drop_duplicates()

# Save the matched rows to a new CSV file (optional)
matched_ids.to_csv('dictionary_cell_lines.csv', index=False)

print("Matching IDs have been saved to 'matched_ids.csv'")
