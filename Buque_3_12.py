#%% 
import pandas as pd 
import numpy as np
import os
import networkx as nx 
import pickle 
# %%
with open('direct_conections_df.pkl','rb')as file:
    data=pickle.load(file)
Conexiones=pd.DataFrame(data)
Conex_1=Conexiones.iloc[0:200,0:6]
# %%
G= nx.from_pandas_edgelist(Conex_1,source='p_cty_code',target='d_cty_code',create_using=nx.DiGraph())
nx.draw_networkx(G)
# %%
# https://www.youtube.com/watch?v=px7ff2_Jeqw