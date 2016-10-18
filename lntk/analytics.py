
import networkx as nx

from lntk import manipulations as m

def compute_node_betweeness(G,new_column_id="betweeness"):
    """
    Updates every node with a new attribute under the key new_column_id. The value of the entry is the node betweeness.

    :param G: a networkx undirected graph
    :param new_column_id: a string that will be the column id for the computed feature
    """
    m.update_network_node_data(G,new_column_id,nx.betweenness_centrality(G))

def compute_node_eigenvect(G,new_column_id="eigenvect",max_iter=1000):
    """
    Updates every node with a new attribute under the key new_column_id. The value of the entry is the node eigenvector centrality.

    :param G: a networkx undirected graph
    :param new_column_id: a string that will be the column id for the computed feature
    :param max_iter : the maximum number of iteration for the eigenvector centrality computation.
    """
    m.update_network_node_data(G, new_column_id,nx.eigenvector_centrality(G, max_iter=max_iter))

def compute_node_closeness(G,new_column_id="closeness"):
    """
    Updates every node with a new attribute under the key new_column_id. The value of the entry is the node closeness.

    :param G: a networkx undirected graph
    :param new_column_id: a string that will be the column id for the computed feature
    """
    m.update_network_node_data(G, new_column_id, nx.closeness_centrality(G))

def compute_edge_betweeness(G,new_column_id="betweeness"):
    """
    Updates every edges with a new attribute under the key new_column_id. The value of the entry is the edge betweeness.

    :param G: a networkx undirected graph
    :param new_column_id: a string that will be the column id for the computed feature
    """
    edge_betweenness = nx.edge_betweenness_centrality(G)
    m.update_network_edge_data(G,new_column_id,edge_betweenness)

#def modularity_cluster(G,new_column_id):
#   pass