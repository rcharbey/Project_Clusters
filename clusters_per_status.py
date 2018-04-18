#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:27:06 2018

@author: raphael
"""

from os import listdir
from os.path import expanduser, isfile
import gzip
from igraph import Graph
import json
import csv

home = expanduser('~')

def open_statuses(ego):
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
    
    print '%s/GALLERY/three/%s/Graphs/friends.gml' % (home, ego)
    graph = Graph.Read_GML('%s/GALLERY/three/%s/Graphs/friends.gml' % (home, ego))
    if graph.vs[0].attribute_names().get('name', -1) == -1:
        continue
    if graph.vs[0].attribute_names().get('cluter', -1) == -1:
        continue
    cluster_per_alter = {v['name'] : int(v['cluster']) for v in graph.vs}
    clusters_per_status = {}
    
    statuses = open_statuses(ego)
    for line in statuses:
        status = json.loads(line)
        commenters_for_this_status = []
        if not 'comments' in status:
            continue
        for comment in status.get('comments', []):
            commenter = comment['from']['id']
            if commenter == ego:
                commenters_for_this_status.append('ego')
            else:
                commenters_for_this_status.append(cluster_per_alter.get(commenter, -1))
        
        clusters_per_status[status['id']] = commenters_for_this_status
        
    with open('%s/GALLERY_STATUSES/Clusters_per_status/%s.csv' % (home, ego), 'w') as to_write:
        csvw = csv.writer(to_write, delimiter = ';')
        for status in clusters_per_status:
            csvw.writerow([status] + clusters_per_status[status])