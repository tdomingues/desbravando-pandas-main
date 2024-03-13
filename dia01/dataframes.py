#%%
import pandas as pd

# %%

data = {
    'nome': ['Tamires', 'Luis', 'Tania', 'Alecsandro'],
    'sobrenome': ['Domingues', 'Domingues', 'Domingues', 'Domingues'],
    'idade':[36,69,66,45]
}

#%%
data['idade'][0]

#%%

df = pd.DataFrame(data)
df


# %%

df['idade'].iloc[0]

# %%
df['nome']
# %%

df.info(memory_usage='deep')
# %%

df.describe()
# %%

df.head(2)
# %%

df.tail(2)
# %%
