# Combining-Structural-and-Bioactivity-descriptors
files and scripts used for the study

## Paper
This code comes from the folowing paper, and was modified to fit our needs.

Laufkötter, Oliver, Noé Sturm, Jürgen Bajorath, Hongming Chen, and Ola Engkvist. ‘Combining Structural and Bioactivity-Based Fingerprints Improves Prediction Performance and Scaffold Hopping Capability’. Journal of Cheminformatics 11, no. 1 (8 August 2019): 54. https://doi.org/10.1186/s13321-019-0376-1.



# Data
The raw HTS data can be downloaded at the following link: https://figshare.com/articles/pubchemAssaysRAW_zip/7800554

The raw data represents 582 public assays from PubChem, with thousands of molecules each. In total, there are 715233 unique chemical identifiers (CID), although some of them might be associated to the same molecules. 

The data being very sparse, a code was added to eliminate molecules or assays where too many data points are missing, thus generating denser datasets. 
The dense data can be downloaded in the **htsfp_gen_out/dense** folder on the link https://drive.google.com/drive/folders/1cyK0Y8neZOUdNDU1UCkM-s4EQEdr_Gw9

