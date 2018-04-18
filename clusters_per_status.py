#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:27:06 2018

@author: raphael
"""

from os import listdir, isfile
from os.path import expanduser
import gzip
from igraph import Graph
import json
import csv

home = expanduser('~')

def open_statuses(ego, name):
    path = expanduser('~/data/three/%s/statuses.jsons' % ego)

    if isfile(path):
        f = open(path, 'rb')
    else:
        gz = path+".gz"
        f = gzip.open(gz, 'rb')
    return f

for ego in listdir('%s/data/three/' % home):
    if ego[0] != 'a':
        continue
    
    graph = Graph.ReadGML('%s/GALLERY/three/%s/Graphs/friends.gml' % (home, ego))
    cluster_per_alter = {v['name'] : v['cluster'] for v in graph.vs}
    clusters_per_status = {}
    
    
    statuses = open_statuses(ego)
    for line in statuses:
        status = json.load(line)
        commenters_for_this_status = []
        for comment in status['comments']:
            commenter = comment['from']['id']
            if commenter == ego:
                commenters_for_this_status.append('ego')
            else:
                commenters_for_this_status.append(clusters_per_status.get(commenter, -1))
        
        clusters_per_status[status['id']] = commenters_for_this_status
        
    with open('%s/GALLERY_STATUSES/Clusters_per_status/%s.csv' % (home, ego), 'w') as to_write:
        csvw = csv.writer(to_write, delimiter = ';')
        for status in clusters_per_status:
            csvw.writerow([status] + clusters_per_status[status])
        