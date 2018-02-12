# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:46:20 2018

@author: raphael
"""

from igraph import *

def clutering(ego):
    graph = Graph.read_gml('../DATA/$s.gml' % ego)
    clusters_list = graph.community_multilevel()
    _cc_list = graph.decompose()
    cluster_per_alter = {}
    index = 0
    for cc in _cc_list:
        for alter in cc:
            cluster_per_alter[cc] = index
        index += 1