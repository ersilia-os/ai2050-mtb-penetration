# ai2050-mtb-penetration

This repository contains data curation and modelling related to permeability across M.tb cell wall and M.tb lesions

## Data
- [Valitalo et al, 2016](https://link.springer.com/article/10.1007/s11095-015-1832-x): prediction of Epithelial Lining Fluid (ELF)-plasma concentration ratio based on clinical data.
- [Sarathy et al, 2016](https://pubmed.ncbi.nlm.nih.gov/27626295/): drug penetration in tuberculosis lesions, measured by undiluted fraction unbound (FU). Passive drug diffusion through caseum _in vivo_ increases as the fraction unbound of drug in caseum _ex vivo_ increases. 279 molecules were tested and results are available in percentage of FU (higher percentage, higher diffusion).
- [Janardhan et al, 2016](https://pubs.rsc.org/en/content/articlelanding/2016/mb/c6mb00457a): permeability through _M.tb_ cell wall based on inferred data: molecules active in enzymatic assays but not whole cell data are assumed to be non-permeable and the other way around.
- [Valitalo et al, 2016](https://link.springer.com/article/10.1007/s11095-015-1832-x): prediction of Epithelial Lining Fluid (ELF)-plasma concentration ratio (EPR) based on clinical data. Per each molecule (56 in total), one or several clinical measures are obtained, in LogEPR. Higher values therefore indicate better availability in the lungs.
- [Radchenko et al, 2023](https://www.mdpi.com/1420-3049/28/2/633): Curation of PubChem to identify M.tb cell wall penetrating compounds: molecules active in enzymatic assays but not whole cell data are assumed to be non-permeable and the other way around. A dataset named MTBPen is generated with 5371 compounds (2671 penetrating vs 2700 non-penetrating)
- [Lepori et al, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11888444/): use of click-chemistry (PAC-MAN) to identify permeable compounds in a dataset of 1500 molecules (MycoPermeNet: https://github.com/Nevbarunegbe/Mycomembrane-permeability-project). The target variable is the standardised residual fluorescence relative to the baseline. Higher residual fluorescence means the chemical did not penetrate the cell (positive values) and lower residual fluorescence indicates higher permeability.
- [Merget et al, 2012](https://academic.oup.com/bioinformatics/article/29/1/62/272745): using CDD TB data, permeability is assessed using ZINC as negative data.
- [Richter et al, 2017](https://www.nature.com/articles/nature22308): establishment of rules for molecule accumulation in _E.coli_. The chemical features in the rules established in this paper are calculated to build an entry score.

### Discarded papers:
- [Banerjee et al, 2024](https://link.springer.com/article/10.1007/s11030-024-10952-3): data not available, simple models trained on 5368 compounds (could be the MtbPen dataset)
- [Wibowo et al, 2025](https://www.sciencedirect.com/science/article/abs/pii/S0169743924002053): re-doing of MTbPen model (https://github.com/asw1982/MTbPrediction/tree/main)
- [Sullivan et al, 2024](https://www.biorxiv.org/content/10.1101/2024.12.15.628588v1.full): accumulation of molecules in M.abscessus, measured by LC-MS. Data not public yet.


## About the Ersilia Open Source Initiative

The [Ersilia Open Source Initiative](https://ersilia.io) is a tech-nonprofit organization fueling sustainable research in the Global South. Ersilia's main asset is the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia), an open-source repository of AI/ML models for antimicrobial drug discovery.

![Ersilia Logo](assets/Ersilia_Brand.png)
