#%%

import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df
# %%

df.head(5)
df.tail(5)
# %%


colunas = [
            "UUID",
            "Points",
            "IdCustomer",
            "DtTransaction"]


df = df[colunas]
df
# %%
