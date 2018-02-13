# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:46:20 2018

@author: raphael
"""

from igraph import *
import os
import csv

def compute_clustering(graph):
    cluster_per_alter = {}
    for alter in graph.vs:
        cluster_per_alter[alter['name']] = alter['cluster']
    return cluster_per_alter
        

def main():
    with open('../Data/clusters_per_alters.csv', 'w') as to_write:
        csvw = csv.writer(to_write, delimiter = ';')
        csvw.writerow(['ego','alter', 'cluster' ])        
        
        for graph_name in os.listdir('../Data/Graphs'):
            ego = graph_name.split('.')[0]
            graph = Graph.Read_GML('../Data/Graphs/%s' % graph_name)
            
            clustering = compute_clustering(graph)
            
            for alter in clustering:
                csv.writerow([ego, alter, clustering[alter]])
                
if __name__ == '__main__':
    main()
        
        