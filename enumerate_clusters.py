# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:41:37 2018

@author: raphael
"""

from igraph import *
import os
import csv

import sys
sys.path.append('/home/algopolapp/Project_Clusters/Scripts/EGOPOL/Enumeration/')
import enumerate_patterns

def read_clustering(ego):
    with open('../Data/Clusters_per_ego/%s.csv' % ego, 'r') as to_read:
        csvr = csv.reader(to_read, delimiter = ';')
        entete = csvr.next()
        
        alters_per_cluster = {}
        
        for line in csvr:
            alter, cluster = line
            if not cluster in alters_per_cluster:
                alters_per_cluster[cluster] = []
            alters_per_cluster[cluster].append(alter)
    
    return alters_per_cluster
        

def main():
    for graph_name in os.listdir('../Data/Graphs/'):
        ego = graph_name.split('.')[0]
        clusters = read_clustering(ego)
        graph = Graph.Read_GML('../Data/Graphs/%s' % graph_name)  
        
        
        with open('../Patterns_per_ego/%s.csv' % ego, 'w') as to_write:
            csvw = csv.writer(to_write, delimiter = ';')            
            csvw.writerow(['cluster'] + ['pattern %s' % i for i in range(1,31)])            
            
            for cluster in clusters:
                gcluster = graph.subgraph(cluster)
        
                pt, ps = enumerate_patterns.characterize_with_patterns(cluster, 5)

                csvw.writerow([clusters.index(cluster)] + pt)
                
        
        
if __name__ == '__main__':
    main()