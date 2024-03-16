#%%

import pandas as pd
import datetime
df = pd.read_excel("../data/transactions.xlsx")
df
# %%

condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user["Points"].sum()

# %%

df_sumary = df.groupby(["IdCustomer"])["Points"].sum()
df_sumary.reset_index()
# %%

df.groupby(["IdCustomer"]).agg({"Points": "sum",
                                 "UUID": "count", 
                                 "DtTransaction": "max"}).rename(columns={"Points": "Pontos",
                                 "UUID": "Frequencia", 
                                 "DtTransaction": "UltimaData"}).reset_index()

# %%




# %%

data1 = df["DtTransaction"][0]
(now - data1).days

# %%

condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
diff = datetime.datetime.now() - df_user["DtTransaction"].max()
diff


# %%

def recencia(x):
    diff datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(["IdCustomer"]).agg({"Points": "sum",
                                 "UUID": "count", 
                                 "DtTransaction": recencia}).rename(columns={"Points": "Pontos",
                                 "UUID": "Frequencia", 
                                 "DtTransaction": "UltimaData"}).reset_index()
)
# %%
