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
# %%
current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"/Users/usuario/Desktop/jira_sample.csv")
J=pd.read_csv(filename,delimiter=',', decimal='.')

# %%
import numpy as np 
am=pd.DataFrame(np.zeros(shape=(30,30)))
# %%

# %%
for country in J[J['Reporter'].str.contains('doll')]['Assignee'].unique():
    
    for species in list(J[(J['Assignee'] == country) & (J['Reporter'].str.contains('Native'))]['Creator']):
        
        for invaded_country in J[(J['Creator'] == species) & (J['Reporter'] == 'lee')]['Assignee']:
        
            am.at[invaded_country,country] += 1

# %% Grafico de df a networkx (a través de edgelist)
G= nx.Graph()
J1= J[['Assignee','Reporter']]
G= nx.from_pandas_edgelist(J1,'Assignee','Reporter')

from matplotlib.pyplot import figure
figure(figsize=(10,8))
nx.draw_shell(G,with_labels=True)
# %%  Grafico de df a networkx (a través de adjacency)
G= nx.from_pandas_adjacency(Z)

# %%
#                   CREAR TABLA DINAMICA


# %%       GRAFICO 1  (DF to NX)

# Una vez se ha cargado la base de datos como df, creamos otro df con las columnas de interés
# Creamos un gráfico vacio  --> G=nx.Graph()  //  e introducimos el nuevo df mediante el comando G= nx.from_pandas_edgelist(df,'col 1','col 2',...,)
# Por último, con matplotlib graficamos:

# from matplotlib.pyplot import figure
# figure(figsize=(10, 8))
# nx.draw_shell(G, with_labels=True)

# Luego para comprobar las conexiones con un nodo concreto usamos G['nodo name']
# Mediante el comando len(G['nodo name']) nos devuelve cuantas conexiones tiene dicho nodo

# si quisieramos crear otro df que muestre los nodos y su numero de conexiones usamos:
leaderboard = {}
for x in G.nodes:
 leaderboard[x] = len(G[x])
s = pd.Series(leaderboard, name='connections')
df2 = s.to_frame().sort_values('connections', ascending=False)

# %%        Cambiar la matriz por datos binarios (método 1)
#for i in Z1:
 #   Z1[i]=np.where(Z1[i]>4000,1,0)
# %%        Cambiar la matriz por datos binarios (método 1)
Z2=Z.stack()
Z2=pd.DataFrame(Z2)
Z2=Z2.reset_index()
Z_2=Z2.rename(columns={'index':'Salida','level_1':'Entrada',0:'Value'})
Z_2['Important']=np.where(Z_2['Value']>10000,1,0)
#Z_2.drop(Z_2.loc[Z_2['Important']==0].index, inplace=True)
# %%

