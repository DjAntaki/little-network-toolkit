
import networkx as nx
from src.scripts.manipulations import *

def compute_node_betweeness(G,new_column_id="betweeness"):
    """
    Updates every node with a new entry under the key new_column_id. The value of the entry is the node betweeness

    :param G:
    :param new_column_id:
    :return:
    """
    update_network_node_data(G,new_column_id,nx.betweenness_centrality(G))

    return G

def compute_node_eigenvect(G,new_column_id="eigenvect"):
    update_network_node_data(G, new_column_id,nx.eigenvector_centrality(G, max_iter=1000))
    return G

def compute_node_closeness(G,new_column_id="closeness"):
    update_network_node_data(G, new_column_id, nx.closeness_centrality(G))
    return G

def compute_edge_betweeness(G,new_column_id="betweeness"):
    edge_betweenness = nx.edge_betweenness_centrality(G)
    update_network_edge_data(G,new_column_id,edge_betweenness)
    return G