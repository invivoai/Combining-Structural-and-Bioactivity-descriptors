
import time
import sys, os
import pandas as pd
import numpy as np
import math
# import pubchempy as pcp
from ivbase.utils.datasets.pubchem import get_smiles


print('You can download all the CID-SMILES conversion here:\n'+
    'ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-SMILES.gz')

if len(sys.argv) != 3:
	print ('Usage : python ' + sys.argv[0] + ' [ dict_aggregate folder  ]' + ' [ output_file ]')
	exit()


folder = sys.argv[1]
all_cid = []
file_list = os.listdir(folder)
output_file = sys.argv[2]

# Read all TSV files, and get all the used CIDs
for ii, file in enumerate(file_list):
    fullfile = os.path.join(folder, file)
    df = pd.read_csv(fullfile, sep='\t')
    all_cid += df['CID'].tolist()
    print(f'reading file:{fullfile}    ({ii}/{len(file_list)})')

# Keep only unique CIDs
unique_cid = np.unique(np.array(all_cid)).tolist()
unique_smiles = get_smiles(unique_cid)

# # Convert the CIDS to SMILES
# unique_smiles = []
# block = 100
# for ii in range(math.ceil(len(unique_cid)/block)):
#     print(f'converting pubchem CID to SMILES    ({ii*block}/{len(unique_cid)})')
#     compounds = pcp.get_compounds(unique_cid[ii*block:(ii+1)*block])
#     this_smiles = [c.isomeric_smiles for c in compounds]
#     unique_smiles.extend(this_smiles)
# print('CID conversion done!')



# Save the CID conversion file
df = pd.DataFrame({'CID': unique_cid})
df['SMILES'] = unique_smiles
df.to_csv(output_file, header=False, index=False, sep='\t')

print('DONE!')


