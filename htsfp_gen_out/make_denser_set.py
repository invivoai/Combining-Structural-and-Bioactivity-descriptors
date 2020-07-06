# %% Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% Read CSV data
filename = 'htsfp_t20000'
df = pd.read_csv(filename + '.csv', index_col=0)

# %% Replace N, A and x by numerical values
df.replace(to_replace={'x': float('nan'), 'A': 1., 'N': 0.}, inplace=True)

# %% Count the number of non-nan elements in each row
smiles_col = 'SMILES'
smiles = df[smiles_col]
df.drop(columns=smiles_col, inplace=True)
counts_x = df.isna().T.sum()

# %% Remove rows with too many nans and columns with not enough activity

for sparse_col_th in [0, 0.001, 0.005]:
    for th in range(40, 161, 20):

        # Remove rows with too many nans
        this_counts = counts_x <= th
        print(f'number of elements at threshold <= {th}:   {np.sum(this_counts)}')
        dense_df = df.iloc[this_counts.values]
        dense_smiles = smiles[this_counts.values]

        # Remove columns with not enough activity
        dense_no_nan = np.nan_to_num(dense_df.values)
        mean = np.nanmean(dense_no_nan, axis=0)
        is_sparse_col = (mean > sparse_col_th) & (~np.isnan(mean))
        dense_df = dense_df.iloc[:, is_sparse_col]
        dense_df.insert(0, smiles_col, dense_smiles)
        print(f'number of columns removed at th {sparse_col_th}: {df.shape[1] - dense_df.shape[1]}')

        dense_df.to_csv(f'dense/{filename}_dense_row-th-{th}_col-th-{sparse_col_th}.csv')


# %%
