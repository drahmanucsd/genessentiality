import pandas as pd
import matplotlib.pyplot as plt
aggregated_results = pd.read_csv("Initial datasets/aggregated_results.csv")
target_genes = pd.read_excel("Initial datasets/ecDNA Target genes.xlsx")
scores = pd.read_csv("CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv")
cell_line_converter = pd.read_csv("DepMap-celllines.csv")

aggregated_results = pd.DataFrame(aggregated_results, columns=['Sample name','Classification'])
# Function to replace 'yes' with 'pos' and anything else with 'neg'
aggregated_results['Classification'] = aggregated_results['Classification'].apply(lambda x: 'pos' if x == 'ecDNA' else 'neg')
merged_df = aggregated_results.merge(cell_line_converter, left_on='Sample name', right_on='CCLE_Name', how='left')
merged_df = merged_df.merge(scores, left_on='Broad_ID', right_on='cell_id', how='left')
reduced_df = merged_df.drop(columns=['Sample name','Broad_ID','CCLE_Name','Aliases','COSMIC_ID','Sanger ID','Gender','Primary Disease','Subtype Disease','Source'])

pos_list =[]
neg_list = []
def filter_row(row):
    return [x for x in row if isinstance(x, float) and not pd.isna(x)]

# Iterate through each row in the dataframe
for index, row in reduced_df.iterrows():
    filtered_row = filter_row(row.values)
    if row['Classification'] == 'pos':
        [pos_list.append(x) for x in filtered_row]
    elif row['Classification'] == 'neg':
        [neg_list.append(x) for x in filtered_row]
merged_df.to_csv('merged_data.csv', index=False)

fig, ax = plt.subplots()

# Create histograms for positive and negative scores with density=True
ax.hist([pos_list, neg_list], bins=10, label=['Positive', 'Negative'], density=True)

# Convert y-axis ticks to percentages
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))

# Set labels and title
ax.set_xlabel('Score')
ax.set_ylabel('Relative Frequency')
ax.set_title('Histogram of Positive and Negative Scores')

# Add legend
ax.legend()

# Show plot
plt.show()