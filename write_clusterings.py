# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:02:50 2018

@author: raphael
"""

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
        
        if not 'cluster' in alter.attribute_names():
            cluster_per_alter = {}
            clusters_list = graph.community_multilevel()
            for cluster in clusters_list:
                for alter in graph.vs:
                    cluster_per_alter[alter['name']] = alter['id']
            break
        cluster_per_alter[alter['name']] = str(int(alter['cluster']))
    
    return cluster_per_alter
        

def main():        
        for graph_name in os.listdir('../Data/Graphs'):
            ego = graph_name.split('.')[0]
            graph = Graph.Read_GML('../Data/Graphs/%s' % graph_name)
            
            clustering = compute_clustering(graph)
            
            with open('../Data/Clusters_per_ego/%s.csv' % ego, 'w') as to_write:
                csvw = csv.writer(to_write, delimiter = ';')
                csvw.writerow(['alter', 'cluster' ])                  
        
                for alter in clustering:
                    csvw.writerow([alter, clustering[alter]])
                
if __name__ == '__main__':
    main()