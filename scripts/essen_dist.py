import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

# Path to cell ID chart and essentiality scores
scp = "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv"
sc_df = pd.read_csv(scp)
r, c = sc_df.shape

# Loop through each column (excluding the first one, assuming it's the cell ID column)
for i in range(1, c):
    gene = sc_df.columns[i]
    scs = sc_df[gene].dropna().tolist()

    # Calculate mean and standard deviation
    mean, std, med = stats.mean(scs), stats.stdev(scs), stats.median(scs)
    
    # Plot histogram
    plt.hist(scs, bins=30, edgecolor='black')  # You can adjust the number of bins as needed
    plt.gca().invert_yaxis()
    plt.title(gene + "\n" + str(med)[:9])
    plt.xlabel("Essentiality Score")
    plt.ylabel("Frequency")
    
    # Save the plot
    plt.savefig("Essentiality_Plots/" + gene + ".png", format='png')
    plt.clf()
