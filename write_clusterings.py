# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:46:20 2018

@author: raphael
"""

from igraph import *
import os
import csv

def compute_clutering(graph):
    clusters_list = graph.community_multilevel()
    _cc_list = graph.decompose()
    cluster_per_alter = {}
    index = 0
    for cc in _cc_list:
        for alter in cc:
            cluster_per_alter[cc] = index
        index += 1
        

def main():
    with open('../Data/clusters_per_alters.csv', 'w') as to_write:
        csvw = csv.writer(to_write, delimiter = ';')
        csvw.writerow(['ego','alter', 'cluster' ])        
        
        for graph_name in os.listdir('../Data/Graphs'):
            ego = graph_name.split('.')[0]
            graph = Graph.read_gml('../Data/Graphs/$s.gml' % graph_name)
            
            clustering = compute_clustering(graph)
            
            for alter in clustering:
                csv.writerow([ego, alter, clustering[alter]])
                
if __name__ == '__main__':
    main()
        
        