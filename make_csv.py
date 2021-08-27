import gzip
import csv
import os
import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def unzip_tsv_gz_and_write_to_csv(tsv_gz_path, csv_path):
    with gzip.open(tsv_gz_path, 'rt') as f:
        tsv_reader = csv.reader(f, delimiter="\t")
        with open(csv_path, 'w') as new_csv:
            csv_writer = csv.writer(new_csv, delimiter=',')
            for line in tsv_reader:
                csv_writer.writerow(line)

csv_path_labels = os.path.join('resources', 'butterfly_labels.csv')
unzip_tsv_gz_and_write_to_csv('resources\SS-Butterfly_labels.tsv.gz', 
                            csv_path_labels)

csv_path_weights = os.path.join('resources', 'butterfly_weights.csv')
unzip_tsv_gz_and_write_to_csv('resources\SS-Butterfly_weights.tsv.gz', 
                            csv_path_weights)

edge_df = pd.read_csv(csv_path_weights)
node_df = pd.read_csv(csv_path_labels)
g = nx.Graph()
g.add_node_from(node_df['# Node_ID'])
