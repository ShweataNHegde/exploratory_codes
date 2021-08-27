import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
csv_path_labels = os.path.join('resources', 'butterfly_labels.csv')
csv_path_weights = os.path.join('resources', 'butterfly_weights.csv')

edge_df = pd.read_csv(csv_path_weights)
node_df = pd.read_csv(csv_path_labels)
g = nx.Graph()
g.add_nodes_from(node_df['# Node_ID'])
for index, row in edge_df.iterrows():
    g.add_edge(row["# NodeID1"], row["NodeID2"])

nx.draw(g)
plt.savefig("butterfly_graph.png")

# Data from http://snap.stanford.edu/biodata/datasets/10029/10029-SS-Butterfly.html
