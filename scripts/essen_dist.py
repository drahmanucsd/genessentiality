import pandas as pd, matplotlib.pyplot as plt, statistics as stats

#path to cell ID chart and essentialiry scores
scp = "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv"
sc_df = pd.read_csv(scp)
r,c = sc_df.shape

for i in range(1,c):
    cid = list()
    gene = sc_df.columns[i]
    scs = sc_df[gene].dropna().tolist()
    scs.sort()
    mean, std = stats.mean(scs), stats.stdev(scs)
    plt.bar(range(len(scs)),scs)
    plt.xticks([])
    plt.gca().invert_yaxis()
    plt.title(gene + "\n" + str(mean)[:9] + "±" + str(std)[:9])
    plt.ylabel("Essentiality Score")
    plt.savefig("Plots/" + gene + ".png",format = 'png')
    plt.clf()