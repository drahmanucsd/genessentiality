![project_status](https://img.shields.io/badge/project%20status-stable-green)
![python](https://img.shields.io/badge/python-3.9.6-green)
![pandas](https://img.shields.io/badge/pandas-2.2.2-white)

# genessentiality
Using Depmap to test the essentiallity of genes impact on different cancer cell lines

Data based on this paper: 
https://www.biorxiv.org/content/10.1101/2023.04.24.537925v1

## Repository Overview:

### Scripts
Houses all python scripts that were used to manipulate the gene lists, and obtain DP cell lines for us to input into the [DepMap download page](https://depmap.org/portal/download/custom/).

#### gene_name_dict_matching.py
* This is a script used to 

### Output files
Houses all output files from different scripts

## Initial datasets
Contains `aggregated_results.csv` which was the total results data taken from the paper, and `ecDNA Targer genes.xlsx`, which had our initial gene list in it.

### Intermediate data
Houses DepMap Broad ID's for cell lines, and our extracted gene_lists

### DP Inputs
Contains all of the input data that we fed DepMap to obtain essentiality scores, includes `DP_cell_line_ID.csv` which is the converted cell lines from DepMap, and `final_DP_gene_inputs.txt`, which is the list of genes that was filtered for key errors using `gene_name_dict_matching.py`

## Pipeline Description:
### Obtaining data
Given a list of list of gene data we extracted and filtered the particular genes ("~/filter.py") of interest from this file "~/ecDNA Target genes.xlsx". This extracted data further needed manual cleaning in the form of matching aliases with the primary name associated with a gene on Depmap "~/extracted_text.txt".

This space seperated list is then used to generate a subdataset which can be downloaded from depmap's [download page](https://depmap.org/portal/download/custom/). 
### Analyzing cell line data
### Plotting
## File Descriptions:
### filter.py
### ecDNA Target genes.xlsx
### extracted_text.txt
