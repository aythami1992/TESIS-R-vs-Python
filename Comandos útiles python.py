#%%
import pandas as pd
import numpy as np
import networkx as nx
import os
 
#%%  Utilizar directorio
current_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"/Users/usuario/Desktop/Z.csv")
Z=pd.read_csv(filename,delimiter=',', decimal='.')
# %%
Z.set_index('index')
# %%
urrent_dir=os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(current_dir,r"/Users/usuario/Desktop/jira_sample.csv")
J=pd.read_csv(filename,delimiter=',', decimal='.')

# %%
