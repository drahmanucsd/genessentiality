![project_status](https://img.shields.io/badge/project%20status-stable-green)
![python](https://img.shields.io/badge/python-3.9.6-green)
![pandas](https://img.shields.io/badge/pandas-2.2.2-white)

# genessentiality
Using DepMap to test the essentiality of genes' impact on different cancer cell lines

Data based on this paper: 
https://www.biorxiv.org/content/10.1101/2023.04.24.537925v1

## Repository Overview

This repository contains scripts and data used to analyze the essentiality of genes in various cancer cell lines with respect to the presence of circular extrachromosomal DNA (ecDNA).

### Directory Structure

#### DP_inputs
- `final_DP_gene_inputs.txt`: Final list of genes after filtering for errors, used as input for DepMap.
- `DP_cell_line_ID.csv`: List of cell lines with their DepMap IDs, used for querying essentiality scores from DepMap.

#### DP_output.csv
- Contains the essentiality scores obtained from DepMap for the genes and cell lines of interest.

#### CRISPR_(DepMap_Public_23Q4+Score,_Chronos)_subsetted.csv
- Subset of CRISPR data from DepMap, containing essentiality scores for specific genes and cell lines.

#### ecDNA_plots
- `ACH-000514.png`, `ACH-000719.png`, `ACH-000097.png`: Example plots showing the distribution of essentiality scores for individual cell lines.
- `neg_ecDNA_content.png`, `pos_ecDNA_content.png`: Plots showing the distribution of essentiality scores for cell lines with negative and positive ecDNA content, respectively.

#### DepMap-celllines.csv
- Contains information about the cell lines used in the analysis, including their DepMap IDs and other relevant metadata.

#### Essentiality_Plots
- `CCDC127.png`, `TMEM203.png`, `OS9.png`, `MFSD14A.png`, `MAK16.png`: Plots showing the distribution of essentiality scores for individual genes.

#### output files
- `ranked_scores.csv`: Contains the ranking of genes based on the significance of the difference in essentiality scores between ecDNA positive and negative cell lines.
- `match.csv`: Contains cell lines with their associated DepMap IDs, ecDNA status, and positive/negative designation.
- `matched_ids.csv`: List of cell lines of interest, used as input for DepMap downloads.

#### scripts
- `essen_dist.py`: Script for generating distribution plots of essentiality scores.
- `ecDNA_corr_plots.py`: Script for generating correlation plots between ecDNA content and essentiality scores.
- `ecDNA_PosNeg_Gene.py`: Script for analyzing essentiality scores for genes with respect to ecDNA status.
- `DP_gene_alias_converter.py`: Converts gene names from the original list to DepMap ID equivalents.
- `visual.py`: Generates graphical plots from the result data.
- `filter.py`: Extracts relevant data for analysis and prepares input files for DepMap.

#### Intermediate data
- `DP_gene_names.txt`: List of DepMap gene names used for querying essentiality scores.
- `og_gene_names.txt`: Original list of gene names extracted from `ecDNA Target genes.xlsx`.

#### Initial datasets
- `ecDNA Target genes.xlsx`: Initial list of target genes.
- `aggregated_results.csv`: Total results data taken from the paper.

### Pipeline Description

#### Obtaining Data
1. Extract the list of target genes from `./Initial datasets/ecDNA Target genes.xlsx` and save it to `./Intermediate data/og_gene_names.txt`.

#### Data Manipulation
1. Run `./scripts/filter.py` to generate `./output files/matched_ids.csv`, which lists cell lines of interest from `aggregated_results.csv` and serves as input for DepMap downloads.
2. Convert gene names to primary DepMap names and save them in `./Intermediate data/DP_gene_names.txt`.

#### Visualization
1. After downloading data from DepMap, convert gene names back to their aliases.
2. Use `./scripts/visual.py` to generate graphical plots of the results.

### Analysis Methodology
1. **Data Preparation:** Download essentiality scores across all genes and cell lines from the DepMap portal. Load this data into a pandas DataFrame (CG matrix).
2. **Conversion of Cell Line IDs:** Use `DP_gene_alias_converter.py` to convert Broad IDs to CCLE names.
3. **Filtering and Categorization:** Use `filter.py` to categorize cell lines as ecDNA positive or negative and prepare input files for DepMap.
4. **Statistical Analysis:** Perform a 2-way rank-sum test (Mann–Whitney U test) to compare the distribution of essentiality scores between ecDNA positive and negative cell lines.
5. **Plotting Results:** Generate histograms, violin plots, and correlation plots to visualize the distribution of essentiality scores and the relationship between ecDNA content and gene essentiality.

### Conclusion
The analysis aims to determine if the presence of ecDNA in cancer cell lines influences the essentiality of specific genes, providing insights into potential targets for cancer therapy. Further investigation is required to clarify the correlation between ecDNA content and gene essentiality.

Feel free to explore the scripts and data provided to reproduce the analysis or adapt it for related research.
