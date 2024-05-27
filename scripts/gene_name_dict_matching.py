import pandas as pd

#gene_names = pd.read_csv("og_gene_names", sep = ' ')
og_gene_list = []
with open("og_gene_names.txt", 'r') as f:
    for line in f:
        og_gene_list = line.split(' ')

dp_alias = []
with open("DP_gene_names.txt", 'r') as f:
    for line in f:
        dp_alias = line.split(' ')
print(len(dp_alias), len(og_gene_list))
errors = "KIAA1967 C6orf145 C20orf20 C8orf41 GSG2 ORC1L FAM64A ORAOV1 TMEM194A SGOL2 CCDC108 MARCH9 FAM179A C10orf26 C9orf25 C5orf33 C20orf111 FAM119B C6orf97 C17orf37 FTSJ2 EPB49 JHDM1D WDR67 UQCC KIAA1797 FAM46C C10orf114 MURC ISPD KIAA0415 C20orf107 C8orf79 TMEM66 SEPT1 C2orf54 SRPR C20orf4 C1orf186 DAK C7orf42 C17orf96 COL4A3BP SLMO2 C5orf20 MS4A8B C10orf140 C4orf21 KIAA0748 GARS GPR110 TXNDC3 SEPP1 FBXO18 C9orf169 SQRDL C20orf106 C1orf192 C17orf72 C2orf39 C1orf230 CCDC135 C1orf172 KIAA1751 RTDR1 YSK4 C20orf151 C7orf23 CCDC64B C9orf171 HIAT1 C10orf125"
error_list = errors.split(' ')
print(error_list)

for i in range(len(og_gene_list)):
    for j in range(len(error_list)):
        if og_gene_list[i] == error_list[j]:
            print(f"converting {og_gene_list[i]} into {dp_alias[i]}")
            og_gene_list[i] = dp_alias[i]

with open("final_DP_gene_inputs.txt", "w") as f:
    for gene in og_gene_list:
        f.write(gene +" ")

