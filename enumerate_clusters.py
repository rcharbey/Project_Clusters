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

import time

def read_clustering(ego):
    with open('../Data/Clusters_per_ego/%s.csv' % ego, 'r') as to_read:
        csvr = csv.reader(to_read, delimiter = ';')
        csvr.next()
        
        alters_per_cluster = {}
        
        for line in csvr:
            alter, cluster = line
            if not cluster in alters_per_cluster:
                alters_per_cluster[cluster] = []
            alters_per_cluster[cluster].append(alter)
    
    return alters_per_cluster
        

def main(list_egos):
    for ego in list_egos:
        graph_name = '%s.gml' % ego
        if not graph_name in os.listdir('../Data/Graphs/'):
            continue
        clusters = read_clustering(ego)
        graph = Graph.Read_GML('../Data/Graphs/%s' % graph_name)    
        
        with open('../Data/Time_per_ego/%s.csv' % ego, 'w') as to_write:
            csvw = csv.writer(to_write, delimiter = ';')
            csvw.writerow(['cluster', 'time'])
        
        with open('../Data/Patterns_per_ego/%s.csv' % ego, 'w') as to_write:
            csvw = csv.writer(to_write, delimiter = ';')            
            csvw.writerow(['cluster'] + ['pattern %s' % i for i in range(1,31)])            
            
            for cluster in clusters:
                start_time = time.time()
                
                cluster_ids = [graph.vs[i] for i in range(len(graph.vs)) 
                            if graph.vs[i]['name'] in clusters[cluster]]      
                
                gcluster = graph.subgraph(cluster_ids)
        
                pt, ps = enumerate_patterns.characterize_with_patterns(gcluster, 5)

                csvw.writerow([cluster] + pt)
                
                with open('../Data/Time_per_ego/%s.csv' % ego, 'a') as to_append:
                    csva = csv.writer(to_append, delimiter = ';')
                    csva.writerow([cluster, time.time() - start_time])
                
        
        
if __name__ == '__main__':
    
    list_egos = []
    with open('../Data/size_per_ego.csv', 'r') as to_read:
        csvr = csv.reader(to_read, delimiter = ';')
        csvr.next()
        for line in csvr:
            list_egos.append(line[0], int(line[1]))
    
    list_egos.sort(lambda x : x[1])
    
    main([ego[0] for ego in list_egos])