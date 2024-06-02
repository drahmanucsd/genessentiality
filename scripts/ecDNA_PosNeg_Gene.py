import pandas as pd, matplotlib.pyplot as plt, statistics as s
from scipy.stats import mannwhitneyu as rank_sum

dict_df, sc_df = pd.read_csv("output files/match.csv"), pd.read_csv("CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv")
pvals = list()
r,c = sc_df.shape

for i in range(1,c):
    gene = sc_df.columns[i]
    ec, pos, neg = list(), list(), list()
    for j, row in sc_df.iterrows():
        if not pd.isna(sc_df.iloc[j,i]):
            cl_df = dict_df[dict_df["DP Cell Line ID"] == sc_df.iloc[j,0]]
            if "pos" in cl_df["ecDNA Content"].values:
                ec.append("pos")
                pos.append(sc_df.iloc[j,i])
            else:
                ec.append("neg")
                neg.append(sc_df.iloc[j,i])
    
    statistics, pval = rank_sum(pos,neg)
    if s.median(pos) < s.median(neg):
        pvals.append((gene,str(pval),"pos"))
    else:
        pvals.append((gene,str(pval),"neg"))
    plt.violinplot([pos, neg], showmeans = False, showmedians = True)
    plt.title(gene + "\np-value: " + str(pval))
    plt.xticks([1,2],["Positive","Negative"])
    plt.xlabel("ecDNA content")
    plt.ylabel("Essentiality score")
    plt.grid(True)
    plt.savefig("ecDNA_Gene/" + gene + ".png", format = "png")
    plt.clf()

pvals.sort(key = lambda x:x[1])
with open("output files/PosNeg_pvals.csv","w") as fp:
    for g,p,e in pvals:
        fp.write(f"{g},{p},{e}\n")