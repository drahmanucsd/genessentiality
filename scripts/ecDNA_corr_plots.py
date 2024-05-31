import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

# Path to cell ID chart and essentiality scores
scp = "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv"
sc_df = pd.read_csv(scp)

match = pd.read_csv("output files/match.csv")

pos_scs = []
neg_scs = []

for index, row in sc_df.iterrows():
    cell_name = row[0]

    for index12, row2 in match.iterrows():
        #print(row2['DP Cell Line ID'])
        if cell_name == row2['DP Cell Line ID']:
            if row2['ecDNA Content'] == "pos":
                pos_scs.extend(row[1:].dropna().tolist())
            else:
                neg_scs.extend(row[1:].dropna().tolist())
        #scs = row[1:].dropna().tolist()

    
# Calculate mean and standard deviation
med = stats.median(pos_scs)
    
# Plot histogram
plt.hist(pos_scs, bins=30, edgecolor='black')  # You can adjust the number of bins as needed
plt.gca().invert_yaxis()
plt.title("pos" + "\n" + str(med)[:9])
plt.xlabel("Essentiality Score")
plt.ylabel("Frequency")
    
# Save the plot
plt.savefig("ecDNA_plots/pos_ecDNA_content.png", format='png')
plt.clf()

# Calculate mean and standard deviation
med2 = stats.median(neg_scs)
    
# Plot histogram
plt.hist(neg_scs, bins=30, edgecolor='black')  # You can adjust the number of bins as needed
plt.gca().invert_yaxis()
plt.title("neg" + "\n" + str(med2)[:9])
plt.xlabel("Essentiality Score")
plt.ylabel("Frequency")
    
# Save the plot
plt.savefig("ecDNA_plots/neg_ecDNA_content.png", format='png')
plt.clf()