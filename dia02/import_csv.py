#%%

import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
# %%

df_customers.shape
# %%
df_customers.info(memory_usage='deep')
# %%

df_customers["Points"].astype(int)
# %%

df_customers["Name"].max()
# %%

condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]["Name"].iloc[0]
# %%

condicao = (df_customers["Points"]>=1000)&(df_customers["Points"]<=2000)
df_customers[condicao].describe()


# %%

df_customers[["UUID", "Name"]]

# %%

colunas = df_customers.columns.tolist()
colunas.sort()
colunas
# %%
df_customers = df_customers[colunas]
# %%

df_customers.rename(columns={"Name": "Nome", "Points": "Pontos"})

# %%
df_customers.rename(columns={"UUID" : "Id"}, inplace=True)
df_customers
# %%
