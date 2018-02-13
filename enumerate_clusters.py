# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:41:37 2018

@author: raphael
"""

from igraph import *
import os
import csv

def read_clutering():
    with open('../Data/clusters_per_alters.csv', 'r') as to_read:
        csvr = csv.reader(to_read, delimiter = ';')
        entete = csvr.next()
        
        clusters_per_ego = {}
        
        for line in csvr:
            ego, alter, cluster = line
            if not ego in clusters_per_ego:
                clusters_per_ego = {}
            clusters_per_ego[ego][alter] = cluster
    
    return clusters_per_ego
        

def main():
    read_clustering()
    
if __name__ == '__main__':
    main()