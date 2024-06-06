import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#thresholds
pval_thresh = 1.30102999566
essen_thresh = 0

#getting data from previous scripts
scores = pd.read_csv("output files/total_scores.csv", sep = '\t')
pvals = pd.read_csv("output files/PosNeg_pvals.csv")

#cutting out unnamed column and renamin Genes col for clarity
scores = scores.iloc[:,1:]
scores.rename(columns={'Genes': 'Gene'}, inplace=True)

# sorting by Gene so that pval and score lines up
scores.sort_values(by = 'Gene', inplace = True)
pvals.sort_values(by = 'Gene', inplace = True)

#merging to get pval and score together
total_data = pd.merge(scores[['Gene', 'Median scores']], pvals[['Gene', 'pval', 'ecDNA dominance']], on='Gene')

total_data['- log10 pval'] = np.log10(total_data['pval'])*-1

print(total_data.head(5))

#creating separate df for sig, non sig, and essential genes
bot = total_data[(total_data['Median scores'] > essen_thresh)&(total_data['- log10 pval']<pval_thresh) | ((total_data['Median scores'] > essen_thresh)) | ((total_data['- log10 pval'] < pval_thresh))]
top = total_data[((total_data['Median scores']< essen_thresh)&(total_data['- log10 pval']>=pval_thresh)) ]

neg = total_data[(total_data['ecDNA dominance'] == 'neg') & ((total_data['Median scores']< essen_thresh) & (total_data['- log10 pval']>=pval_thresh))]
#plotting
plt.scatter(x = bot['Median scores'], y = bot['- log10 pval'], s=3, label = 'Not intresting', color = 'purple')
plt.scatter(x=top['Median scores'], y = top['- log10 pval'], s=10, label = 'ecDNA positive', color = 'green')
plt.scatter(x=neg['Median scores'], y = neg['- log10 pval'], s=10, label = 'ecDNA negative', color = 'red')
#adding gene names
for idx, row in top.iterrows():
    plt.text(row['Median scores'], row['- log10 pval'], row['Gene'], fontsize=6, color='green')

for idx, row in neg.iterrows():
    plt.text(row['Median scores'], row['- log10 pval'], row['Gene'], fontsize=6, color='red')
#legend
plt.axhline(pval_thresh,color="grey",linestyle="--")
plt.axvline(essen_thresh,color="grey",linestyle="--")
plt.xlabel("Median scores")
plt.ylabel("- log10 pval")

plt.title('Dist of Gene essentiality scores based on difference between ecDNA content')

plt.legend()
plt.savefig('score_vs_pval_volcano.png', dpi = 300)
