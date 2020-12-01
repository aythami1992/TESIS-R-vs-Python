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
#                   CREAR TABLA DINAMICA   
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

indexnames_2=Z_2[Z_2['Value']<40000].index 
Z_2.drop(indexnames_2, inplace=True)
Z_2nx=Z_2[['Salida','Entrada']]

# Creamos un gráfico vacio  --> P=nx.Graph()  //  e introducimos el nuevo df mediante el comando G= nx.from_pandas_edgelist(df,'col 1','col 2',...,)

P=nx.Graph()
P=nx.from_pandas_edgelist(Z_2nx,'Salida','Entrada')
# Por último, con matplotlib graficamos:

from matplotlib.pyplot import figure
figure(figsize=(12, 9))
nx.draw_shell(P, with_labels=True)

# Luego para comprobar las conexiones con un nodo concreto usamos P['nodo name']
P['USA_19']
# Mediante el comando len(G['nodo name']) nos devuelve cuantas conexiones tiene dicho nodo
len(P['USA_19'])
# si quisieramos crear otro df que muestre los nodos y su numero de conexiones usamos:
#leaderboard = {}
#for x in P.nodes:
# leaderboard[x] = len(G[x])
#s = pd.Series(leaderboard, name='connections')
#df2 = s.to_frame().sort_values('connections', ascending=False)

# %%

