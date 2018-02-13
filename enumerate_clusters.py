# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:41:37 2018

@author: raphael
"""

from igraph import *
import os
import csv

import sys
sys.path.append('EGOPOL/')
import EGOPOL.enumeration.enumerate

def read_clutering(ego):
    with open('../Data/Clusters_per_alters/%s.csv' % ego, 'r') as to_read:
        csvr = csv.reader(to_read, delimiter = ';')
        entete = csvr.next()
        
        cluster_per_alter = {}
        
        for line in csvr:
            alter, cluster = line
            cluster_per_alter[alter] = cluster
    
    return cluster_per_alter
        

def main():
    for graph_name in os.listdir('../Data/Graphs/'):
        ego = graph_name.split('.')[0]
        clusters = VertexClustering(read_clustering(ego))
        graph = Graph.Read_GML('../Data/Graphs/%s' % graph_name)  
        
        
        with open('../Patterns_per_ego/%s.csv', 'w') as to_write:
            csvw = csv.writer(to_write, delimiter = ';')            
            csvw.writerow(['cluster'] + ['pattern %s' % i for i in range(1,31)])            
            
            for cluster in clusters:
                gcluster = graph.subgraph(cluster)
        
                pt, ps = enumerate.characterize_with_patterns(cluster, 5)

                csvw.writerow([clusters.index(cluster)] + pt)
                
        
        
if __name__ == '__main__':
    main()