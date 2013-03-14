
import numpy as np
import pygraphviz as pg
import sys

from splparser.parser import parse as splparse
from zss.compare import distance as tree_dist
from art import splqueryutils

BYTES_IN_MB = 1048576

DISTFILE = 'distances.npy'

ROWS = 0
COLS = 1

COLORS = ['#006600','#990000','#3333CC','#000000', '#FFCC00']
SHAPES = ['circle', 'triangle', 'square', 'diamond', 'pentagon']

BLACK = '#000000'
CIRCLE = 'circle'
EDGE_LEN_EXPANDER = 10.
ZERO_EDGE_LEN = .01

def output_distance_graph(size, graphfile, distancesfile=DISTFILE, normalize=False):
    seen = {}
    parsetrees = []
    for queries in splqueryutils.get_queries(limit=800*BYTES_IN_MB):
        to_parse = []
        for query in queries: 
            if not query.text in seen:
                to_parse.append(query)
            seen[query.text] = 1
        parsetrees = parsetrees + parse_queries(to_parse)
        sys.stderr.write(str(len(parsetrees)) + '\n')
        if len(parsetrees) > size: break
    print "Computing distances."
    distances = get_parsetree_distances(parsetrees, distancesfile, normalize=normalize)
    plot_query_distance_graph(distances)

def get_parsetree_distances(parsetrees, distancesfile, normalize=False):
    try:
        return read_distance_matrix(distancesfile)
    except IOError as e:
        return build_tree_edit_distance_matrix(parsetrees, normalize=normalize)

def read_distance_matrix(distancefile):
    return np.array(np.load(distancefile))

def build_tree_edit_distance_matrix(parsetrees, normalize=False):
    return build_distance_matrix(parsetrees, tree_dist, normalize=normalize)

def build_distance_matrix(data, distfn, normalize=False):
    m = len(data)
    distances = np.zeros((m,m))
    i = j = 0.
    max_distance = -1e10
    for i in range(m):
        for j in range(i+1, m): # The distance matrix is symmetric.
            p = data[i]
            q = data[j]
            distance = distfn(p, q)
            max_distance = max(max_distance, distance)
            distances[i,j] = distances[j,i] = distance
    if normalize:
        distances = distances / max_distance
    np.save(DISTFILE, distances)    
    return distances

def plot_query_distance_graph(distances, clusteridxs=None, graph_filename="query_clusters.png"):
    
    graph = pg.AGraph()
    
    # node attributes:
    graph.node_attr['style'] = 'filled'
    graph.node_attr['label'] = ' '
    graph.node_attr['height'] = .3
    graph.node_attr['width'] = .3
    graph.node_attr['fixedsize'] = 'true'
    
    num_nodes = distances.shape[ROWS]
    color = BLACK
    shape = CIRCLE 
    for i in range(num_nodes):
        if clusteridxs is not None:
            color,shape = assign_node_color_shape(i, clusteridxs)
        graph.add_node(i, fillcolor=color, shape=shape)    
    
    # edge attributes:
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if distances[i,j] > 0:
                graph.add_edge(i,j, len=distances[i,j]*EDGE_LEN_EXPANDER)
            else:
                graph.add_edge(i,j, len=ZERO_EDGE_LEN)

    graph.edge_attr['style'] = 'setlinewidth(.001)'
    
    graph.layout()
    graph.draw(graph_filename)

def assign_node_color_shape(i, clusteridxs):
    pass


