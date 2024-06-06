import pandas as pd, matplotlib.pyplot as plt, statistics as stats
from scipy import stats as stt
import seaborn as sns

#path to cell ID chart and essentialiry scores
genes, scores = "output files/match.csv", "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv"
genes_df, scores_df = pd.read_csv(genes), pd.read_csv(scores)
# print(cell_df.head())

#rows of the CRISPR are cell line and the columns are the gene name
r,c = scores_df.shape
meta_ep, meta_en = list(), list()

for i in range(1,c):
    #extracting the name of the gene from column of CRISPR file
    gene_name = scores_df.columns[i]

    scs = scores_df.iloc[:,i].dropna().tolist() # Loading scores from every column

    ec, sc = list(), list()
    ep, en = list(), list() # Store the essentiality score of all ecDNA postive and negative

    for j in range(len(scs)):
        #getting the total rows of the CRISPR file, which are the cel line ids
        DP_cell_id = scores_df.iloc[j,0]

        cl_df = genes_df[genes_df["DP Cell Line ID"] == DP_cell_id] # select rows where cell_id is present
        print(cl_df.head(10))
        ec += cl_df["ecDNA Content"].tolist()
        sc += [scs[j]] * cl_df.shape[0]
    
    for k in range(len(ec)):
        if ec[k] == "pos":
            ep.append(sc[k])
        else:
            en.append(sc[k])
    meta_ep += ep
    meta_en += en
    
    ep_mean, ep_sd, en_mean, en_sd = stats.mean(ep), stats.stdev(ep), stats.mean(en), stats.stdev(en)
    
    plt.scatter(ec,sc)
    # plt.text(0,0,"ecDNA pos mean:" + str(ep_mean) + "±" + str(ep_sd))
    # plt.text(1,1,"ecDNA neg mean:" + str(en_mean) + "±" + str(en_sd))
    plt.gca().invert_yaxis()
    plt.xlabel("ecDNA Content")
    plt.ylabel("Essentiality score")
    plt.title(gene_name + "\n" + "ecDNA pos mean:" + str(ep_mean) + "±" + str(ep_sd) + "\n" +  
              "ecDNA neg mean:" + str(en_mean) + "±" + str(en_sd), fontsize = 10)
    plt.savefig("Plots/" + gene_name + ".png", format = 'png')
    plt.clf()

print(stt.ttest_ind(meta_en,meta_ep))