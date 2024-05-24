import pandas as pd

# Specify the relative path to the Excel file
tgp = "ecDNA Target genes.xlsx"
<<<<<<< HEAD
raw_data = "aggregated_results.csv"
file_path = open("match.tsv","w")
=======
>>>>>>> 54a5d22f9a5aa08363ca0f2f98a43e2dfe44425f

# Read the Excel file into a DataFrame
tgdf = pd.read_excel(tgp)
raw_data_df = pd.read_csv(raw_data)

# Assuming the third column index is 2 (indexing starts from 0)
gene_column = tgdf.iloc[:, 2]
sample_col = raw_data_df.iloc[:, 1] # sample col
calss_col = raw_data_df.iloc[:, 4] # class col
gene_col = raw_data_df.iloc[:, 22] # gene col for the smaple

# Extract the text before the character "|" which contains the gene name
gene_name = gene_column.str.split('|').str[0].tolist()

for i in range(len(gene_name)):
    for j in range(len(sample_col)):
        if gene_name[i] in gene_col[j]:

            if calss_col[j] == "ecDNA":
                file_path.write(gene_name[i] + "\t" + sample_col[j] + "\t" + "pos\n")
            else:
                file_path.write(gene_name[i] + "\t" + sample_col[j] + "\t" + "neg\n")

file_path.close()



# # Convert the Series to a single string with space-separated values
# extracted_text_str = ' '.join(extracted_text.dropna().astype(str))

# # Save the string to a text file
# with open('extracted_text.txt', 'w') as f:
#     f.write(extracted_text_str)

# print("Genes extracted successfully.")
