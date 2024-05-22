import pandas as pd

# Specify the relative path to the Excel file
tgp = "ecDNA Target genes.xlsx"
arp = "aggregated_results.csv"
fp = open("match.txt","w")

# Read the Excel file into a DataFrame
tgdf = pd.read_excel(tgp)
ardf = pd.read_csv(arp)

# Assuming the third column index is 2 (indexing starts from 0)
gene_column = tgdf.iloc[:, 2]
sc = ardf.iloc[:, 1] # sample col
cc = ardf.iloc[:, 4] # class col
sg = ardf.iloc[:, 22] # gene col for the smaple

# Extract the text before the character "|"
gn = gene_column.str.split('|').str[0].tolist()
for i in range(len(gn)):
    for j in range(len(sc)):
        if gn[i] in sg[j]:
            if cc[j] == "ecDNA":
                fp.write(gn[i] + "\t" + sc[j] + "\t" + "pos\n")
            else:
                fp.write(gn[i] + "\t" + sc[j] + "\t" + "neg\n")

fp.close()
# # Convert the Series to a single string with space-separated values
# extracted_text_str = ' '.join(extracted_text.dropna().astype(str))

# # Save the string to a text file
# with open('extracted_text.txt', 'w') as f:
#     f.write(extracted_text_str)

# print("Genes extracted successfully.")
