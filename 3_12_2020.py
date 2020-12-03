#%%
import pandas as pd 
import numpy as np
import networkx as nx
import os

#%%  Utilizar directorio
current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"/Users/usuario/Desktop/Z.csv")
Z=pd.read_csv(filename,delimiter=',', decimal='.')
Z=Z.set_index('index')

#%%
Z2=Z.stack()
Z2=pd.DataFrame(Z2)
Z2=Z2.reset_index()
Z_2=Z2.rename(columns={'index':'Salida','level_1':'Entrada',0:'Value'})
# Eliminamos las filas en las que se repita el sector en Salida y Entrada
indexnames_2=Z_2[Z_2['Value']<210000].index 
Z_2.drop(indexnames_2, inplace=True)
indexnames_rep=Z_2[Z_2['Salida']==Z_2['Entrada']].index 
Z_2.drop(indexnames_rep, inplace=True)
Z_2nx=Z_2[['Salida','Entrada']]

# Creo otra matriz para hacer pruebas
Z3=Z.stack()
Z3=pd.DataFrame(Z3)
Z3=Z3.reset_index()
Z_3=Z3.rename(columns={'index':'Salida','level_1':'Entrada',0:'Value'})
# Eliminamos las filas en las que se repita el sector en Salida y Entrada
indexnames_3=Z_3[Z_3['Value']<200000].index 
Z_3.drop(indexnames_3, inplace=True)
indexnames_rep_3=Z_3[Z_3['Salida']==Z_3['Entrada']].index 
Z_3.drop(indexnames_rep_3, inplace=True)
Z_3nx=Z_3[['Salida','Entrada']]
# %%
Z_2draw=nx.DiGraph()
Z_2draw=nx.from_pandas_edgelist(Z_2nx,'Salida','Entrada')
Z_3draw=nx.DiGraph()
Z_3draw=nx.from_pandas_edgelist(Z_3nx,'Salida','Entrada')

len(Z_2draw.nodes())

# %%  Dibujamos
nx.draw_networkx(Z_2draw,with_labels=True, node_color='g')
nx.draw_networkx(Z_3draw, with_labels=True, node_color='b',edge_color='r')

