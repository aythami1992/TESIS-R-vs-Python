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
from matplotlib.pyplot import figure
figure(figsize=(12,9))
#nx.draw_shell(G,with_labels=True)
#nx.draw_circular(G)

nx.degree(G)

#si quisieramos crear otro df que muestre los nodos y su numero de conexiones usamos:
conexion= {}
for x in G.nodes:
    conexion[x] = len(G[x])
s = pd.Series(conexion, name='Conexiones')
df2 = s.to_frame().sort_values('Conexiones', ascending=False)
#%%
# Density
nx.density(G)

# Clustering
nx.clustering(G)
# Similar al comando anterior
for i in nx.clustering(G).items():
    print (i)

# Average clustering
nx.average_clustering(G)

# Diameter
nx.diameter(G)
diameter = nx.diameter(net.to_undirected())
# %%

# %%
# https://www.youtube.com/watch?v=px7ff2_Jeqw
#  Rob Chew, Peter Baumgartner | Connected: A Social Network Analysis Tutorial with NetworkX