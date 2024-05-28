![project_status](https://img.shields.io/badge/project%20status-stable-green)
![python](https://img.shields.io/badge/python-3.9.6-green)
![pandas](https://img.shields.io/badge/pandas-2.2.2-white)

# genessentiality
Using Depmap to test the essentiallity of genes impact on different cancer cell lines

Data based on this paper: 
https://www.biorxiv.org/content/10.1101/2023.04.24.537925v1

## Repository Overview:

***Scripts***
Houses all python scripts that were used to manipulate the gene lists, and obtain DP cell lines for us to input into the [DepMap download page](https://depmap.org/portal/download/custom/).

`DP_gene_alias_converter.py`
* This is a script used to convert some of the gene names from the original list, into their DepMap ID equivalents, since some gene names give input errors when entered in DepMap
* The script first opens the original gene names from `og_gene_names.txt`, their equivalent DepMap gene names are stored in `DP_gene_names.txt` and adds both of these to a list
* The `error_list` is a list of genes that resulted in input errors from DepMap because their name is not recognized
* The script iterates through the original names and the names that resulted in errors and finds these genes from `error_list` and replaces them with the DepMap associated name
* The new list of gene names is saved to `final_DP_gene_inputs.txt` which can be found in the DP Inputs folder
`visual.py`
- This is a script that takes the data from "CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv" and generates the png graphs stored in folder "\~/Plots". 
`filter.py`
- This is a  script that takes in data from "./Raw_Data" and pulls out the relevant data needed for analysis. It first extracts the list of ecDNA that are the focus of analysis. These genes are then matched to cell lines from the "~/Initial Datasets/aggregated_results.csv". This allows us to then generate a positive and negative value for each cell line as well and associate that with a gene. We then generate a file of all the cell lines observed into a single column csv which is one of the inputs for Depmap. The other input format for Depmap is also generated which is a space seperated list of all ecDNA observed. The 3d and final output is csv file with all cell lines, their associated depmap id, ecDNA, and pos/neg which is stored in "./output_files/match.csv"

***Output files***
Houses all output files from different scripts

***Initial datasets***
Contains `aggregated_results.csv` which was the total results data taken from the paper, and `ecDNA Targer genes.xlsx`, which had our initial gene list in it.

***Intermediate data***
Houses DepMap Broad ID's for cell lines, and our extracted gene_lists

***DP Inputs***
Contains all of the input data that we fed DepMap to obtain essentiality scores, includes `DP_cell_line_ID.csv` which is the converted cell lines from DepMap, and `final_DP_gene_inputs.txt`, which is the list of genes that was filtered for key errors using `gene_name_dict_matching.py`

## Pipeline Description:
### Obtaining data
Given the list of target genes "./Initial datasets/ecDNA Target genes.xlsx" We were able to extract the list into a space seperated file "./Intermediate data/og_gene_names.txt". This space seperated list is then used to generate a subdataset which can be downloaded from depmap's [download page](https://depmap.org/portal/download/custom/).  However many of the genes in this list were aliases and not the primary name used by depmap, and had to be manually converted into the primary depmap name which can be found in file "~/Intermediate data/DP_gene_names.txt". "./scripts/filter.py" generates the file "./output files/matched_ids.csv" which contains a list of the particular cell lines of interest from "aggregated_results.csv" and is also used as input for the depmap download. Once the data is downloaded, the gene names are converted back into their alias form and then "./scripts/visual.py" is used to generate the graph plots of the result data. 
