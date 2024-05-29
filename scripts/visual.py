import pandas as pd, matplotlib.pyplot as plt, statistics as stats
from scipy import stats as stt
import seaborn as sns

#path to cell ID chart and essentialiry scores
match_df = pd.read_csv("../output files/match.csv")
score_df = pd.read_csv("../CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv")
pos =[]
neg = []

with open('../Intermediate data/og_gene_names.txt', 'r') as file1:
    file1_content = file1.read()

# Read the content of the second file
with open('../Intermediate data/DP_gene_names.txt', 'r') as file2:
    file2_content = file2.read()

# Split the contents into lists of elements
file1_elements = file1_content.split()
file2_elements = file2_content.split()

# Create the dictionary using zip
gene_dict = dict(zip(file1_elements, file2_elements))

x=0
for index, row in match_df.iterrows():
    pn = row['ecDNA Content']
    gene_id = gene_dict[row['Gene Id']]
    cell_id = row['DP Cell Line ID']
    print(pn,gene_id,cell_id)

    try:
        index = score_df.index[score_df.iloc[:,0] == cell_id].tolist()[0]
        score = score_df[gene_id].iloc[index]
        pos.append(score) if pn == 'pos' else neg.append(score)
    except Exception as e:
        print(f"{cell_id} doesn't exists.")
        x+=1
print(x)
# fig, ax = plt.subplots()

# # Scatter plot for positive values
# ax.scatter(["Positive"]*len(pos), pos, color='blue', label='Positive')

# # Scatter plot for negative values
# ax.scatter(["Negative"]*len(neg), neg, color='red', label='Negative')

# # Invert y-axis
# ax.invert_yaxis()

# # Set labels and title
# ax.set_xlabel('Category')
# ax.set_ylabel('Score')
# ax.set_title('Scatter Plot of Positive and Negative Scores')

# # Show plot
# plt.show()

# data = [pos, neg]

# # Create a figure and axis object
# fig, ax = plt.subplots()

# # Create box plot
# ax.boxplot(data, labels=['Positive', 'Negative'])

# # Invert y-axis
# ax.invert_yaxis()

# # Set labels and title
# ax.set_xlabel('Category')
# ax.set_ylabel('Score')
# ax.set_title('Box Plot of Positive and Negative Scores')

# # Show plot
# plt.show()

# fig, ax = plt.subplots()

# # Create histograms for positive and negative scores
# ax.hist([pos, neg], bins=10, label=['Positive', 'Negative'])


# # Set labels and title
# ax.set_xlabel('Score')
# ax.set_ylabel('Frequency')
# ax.set_title('Histogram of Positive and Negative Scores')

# # Add legend
# ax.legend()

# # Show plot
# plt.show()


fig, ax = plt.subplots()

# Create histograms for positive and negative scores with density=True
ax.hist([pos, neg], bins=10, label=['Positive', 'Negative'], density=True)

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


# sns.histplot(pos, color='blue', alpha=0.5, bins=10, kde=True, label='Positive')
# sns.histplot(neg, color='red', alpha=0.5, bins=10, kde=True, label='Negative')

# # Add trendlines
# sns.kdeplot(pos, color='blue')
# sns.kdeplot(neg, color='red')

# # Add labels and legend
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Positive vs Negative Histogram')
# plt.legend()

# # Show plot
# plt.show()


sns.histplot(pos, color='blue', alpha=0.5, bins=10, kde=True, label='Positive', stat='density')
sns.histplot(neg, color='red', alpha=0.5, bins=10, kde=True, label='Negative', stat='density')

# Add trendlines
sns.kdeplot(pos, color='blue')
sns.kdeplot(neg, color='red')

# Add labels and legend
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Positive vs Negative Histogram (Density)')
plt.legend()

# Show plot
plt.show()