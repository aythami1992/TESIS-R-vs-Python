#%% 
import networkx as nx
import os
#%%         Los epigrafes se corresponden con el libro de Kolaczyc et al (2014) y el codigo es el como se implementa ese epigrafe en Python   
#        2.2 Creating Network Graphs 
#        2.2.1 Undirected and Directed Graphs (R)   
#  --> Directed= g <- graph.formula(1-+2,1-+3,2++3) 
G= nx.DiGraph()
G.add_edge('1','2')
G.add_edge('1','3')
G.add_edge('2','4')
G.add_edge('3','5')
G.add_edge('4','5')
G.add_edge('4','6')
G.add_edge('4','7')
G.add_edge('5','6')
G.add_edge('6','7')
#  --> Undirected= g <- graph.formula(1-2,1-3,2-4,3-5,4-5,4-6,4-7,5-6,6-7)
G1= nx.Graph()
G1.add_edge('1','2')
G1.add_edge('1','3')
G1.add_edge('2','4')
G1.add_edge('3','5')
G1.add_edge('4','5')
G1.add_edge('4','6')
G1.add_edge('4','7')
G1.add_edge('5','6')
G1.add_edge('6','7')

#plot(dg)
nx.draw_networkx(G)
# %%
#        2.2.2 Representation graph
# get.adjacency(g) 
G2= nx.read_adjlist('G_adjlist (1).txt', nodetype=int) # previamente se debe tener la lista creada
G2.edges()

# %%
#        2.2.3 Operations on graph
# > h <- induced.subgraph(g, 1:5) 
# > str(h)
H=G.subgraph(['1','4','6','7'])

# %%          2.3 Decorating Network Graphs
#          2.3.1 Vertex, Edge, and Graph Attributes
#   recall that the names: > V(dg)$name // V(dg)$gender
#Signed networks: Some networks can carry information about friendship or antagonism based on conflict or disagreement
G=nx.Graph()
G.add_edge('A','B', sign='+')
G.add_edge('C','D', sign='-')
# %%
#Other edge atributtes: Edges can carry many other labels or attributes
G=nx.Graph()
G.add_edge('A','B', relation='Family')
G.add_edge('B','C', relation='Coworker')
# %%         2.3.2 Using Data Frames
A= nx.karate_club_graph()  # Te devuelve una matriz tipo dataframe 
Karate=nx.to_pandas_adjacency(A)
# %%
