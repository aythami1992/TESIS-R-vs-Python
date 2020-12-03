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


# %% (Base ejemplo)
current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"/Users/usuario/Desktop/jira_sample.csv")
J=pd.read_csv(filename,delimiter=',', decimal='.')


# %%
#                              POR ADJACENCY MATRIX
#                  (Cambiar la matriz por datos binarios (método 1))
Z2=Z.stack()
Z2=pd.DataFrame(Z2)
Z2=Z2.reset_index()
Z_2=Z2.rename(columns={'index':'Salida','level_1':'Entrada',0:'Value'})
#Z_2['Important']=np.where(Z_2['Value']>10000,1,0)
#Z_2.drop(Z_2.loc[Z_2['Important']==0].index, inplace=True)

#                 (Cambiar la matriz por datos binarios (método 2))
#for i in Z1:
#Z1[i]=np.where(Z1[i]>4000,1,0)


# %%       Pasar un DataFrame a Networkx (DF to NX)

# Una vez se ha cargado la base de datos como df, creamos otro df con las columnas de interés
indexnames_2=Z_2[Z_2['Value']<190000].index 
Z_2.drop(indexnames_2, inplace=True)
indexnames_rep=Z_2[Z_2['Salida']==Z_2['Entrada']].index 
Z_2.drop(indexnames_rep, inplace=True)
Z_2nx=Z_2[['Salida','Entrada']]
#%%
# probar función COMPOSE
Z3=Z.stack()
Z3=pd.DataFrame(Z3)
Z3=Z3.reset_index()
Z_3=Z3.rename(columns={'index':'Salida','level_1':'Entrada',0:'Value'})

indexnames_3=Z_3[Z_3['Value']<170000].index 
Z_3.drop(indexnames_3, inplace=True)
Z_3nx=Z_3[['Salida','Entrada']]
#%%
# Creamos un gráfico vacio  --> P=nx.Graph()  //  e introducimos el nuevo df mediante el comando G= nx.from_pandas_edgelist(df,'col 1','col 2',...,)
Z_2draw=nx.Graph()
Z_2draw=nx.from_pandas_edgelist(Z_2nx,'Salida','Entrada')

Z_3draw=nx.Graph()
Z_3draw=nx.from_pandas_edgelist(Z_3nx,'Salida','Entrada')
#%%
# Por último, con matplotlib graficamos:
from matplotlib.pyplot import figure
figure(figsize=(12, 9))
nx.draw_shell(P, with_labels=True)
#nx.draw_networkx(P, with_labels=True)
# %%
# Luego para comprobar las conexiones con un nodo concreto usamos P['nodo name']
P['JPN_29']
# Mediante el comando len(G['nodo name']) nos devuelve cuantas conexiones tiene dicho nodo
len(P['JPN_29'])


#%%
# si quisieramos crear otro df que muestre los nodos y su numero de conexiones usamos:
conexion= {}
for x in P.nodes:
    conexion[x] = len(P[x])
s = pd.Series(conexion, name='Conexiones')
df2 = s.to_frame().sort_values('Conexiones', ascending=False)

# %%
G = nx.Graph()
G.add_edge(1,2,color='r',weight=2)
G.add_edge(2,3,color='b',weight=4)
G.add_edge(3,4,color='g',weight=6)

# %%
subset = Z_2nx[['Salida', 'Entrada']]
tuples = [tuple(x) for x in subset.values]
# %%
pos = nx.circular_layout(G)

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]

nx.draw(G, pos, edges=edges, edge_color=colors, width=weights)

# %%
#############

Z_2draw.nodes()
len(Z_2draw.nodes())
len(Z_2draw.edges())
## Visualitation
# nx.draw  // nx.draw_network
# nx.draw(Z_3draw, with_labels=True, node_color='g')
nx.draw_networkx(Z_2draw)


# %%
