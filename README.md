![project_status](https://img.shields.io/badge/project%20status-stable-green)
![python](https://img.shields.io/badge/python-3.9.6-green)
![pandas](https://img.shields.io/badge/pandas-2.2.2-white)

# genessentiality
Using Depmap to test the essentiallity of genes impact on different cancer cell lines

Data based on this paper: 
https://www.biorxiv.org/content/10.1101/2023.04.24.537925v1

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
