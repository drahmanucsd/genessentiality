import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

#path to cell ID chart and essentialiry scores
cp, scp = "output files/match.csv", "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv"
cell_df, sc_df = pd.read_csv(cp), pd.read_csv(scp)
# print(cell_df.head())

r,c = sc_df.shape
for i in range(1,c):
    gene = sc_df.columns[i]
    scs = sc_df.iloc[:,i].tolist() # Loading scores from every column
    ec, sc = list(), list()
    for j in range(len(scs)):
        cell_id = sc_df.iloc[j,0]
        cl_df = cell_df[cell_df["DP Cell Line ID"] == cell_id] # select rows where cell_id is present
        ec += cl_df["ecDNA Content"].tolist()
        sc += [scs[j]] * cl_df.shape[0]
    
    plt.scatter(ec,sc)
    plt.xlabel("ecDNA Content")
    plt.ylabel("Essentiality score")
    plt.title(gene)
    plt.savefig("Plots/" + gene + ".png", format = 'png')
    plt.clf()