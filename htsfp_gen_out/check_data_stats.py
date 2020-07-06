# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%

df = pd.read_csv('htsfp_t20000.csv', index_col=0)

# %%
counts_x = (df == 'x').T.sum()

# %%
for th in range(40, 201, 40):
    this_counts = counts_x <= th
    print(f'number of elements at threshold <= {th}:   {np.sum(this_counts)}')
    this_index = np.where(this_counts)[0]
    this_hist = plt.hist(this_index, bins=100, alpha=0.2)

plt.show()



# %%
df.replace(to_replace={'x': float('nan'), 'A': 1., 'N': 0.}, inplace=True)


#%%

for th in range(40, 201, 40):
    this_counts = counts_x <= th
    print(f'number of elements at threshold <= {th}:   {np.sum(this_counts)}')
    this_index = np.where(this_counts)[0]
    this_df = df.iloc[this_index, :]
    mean = np.nansum(this_df, axis=0)
    plt.bar(x=np.arange(len(mean)), height=mean, alpha=0.2)

plt.show()

# %%
from sklearn.decomposition import PCA

this_index = np.where(counts_x <= 60)[0]
this_df = df.iloc[this_index, :]
vals = np.nan_to_num(this_df.values)

n_components = np.arange(20, vals.shape[1], 20)
pca_exp_var = []

for n in n_components:
    pca_obj = PCA(n_components=n)
    pca_vals = pca_obj.fit_transform(vals)
    pca_exp_var.append(pca_obj.explained_variance_ratio_.sum())
    print(f'n = {n} ,   explained variance = {pca_exp_var[-1]}')
    

# %%
plt.plot(n_components, 100 * np.array(pca_exp_var))
plt.xlabel('PCA n-components')
plt.ylabel('% of Explained variance')




# %%
