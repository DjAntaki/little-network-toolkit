
def merge_nodes(G, nodes_to_merge, new_node_id):
    """
    Merges a list of nodes in a graph

    :param G: a networkx graph
    :param nodes_to_merge: a list of node ids
    :param new_node_id: an id for the new node
    :return:
    """
    G.add_node(new_node_id)

    edge_list = []
    edge_to_remove = []
    for t,f in G.edges():

        first = False
        if t in nodes_to_merge:
            first = True
        if f in nodes_to_merge:
            if first :
                continue
        else :
            continue

        kwargs = G[t][f]

        if first :
            edge_list.append((new_node_id, f, kwargs))
        else :
            edge_list.append((t, new_node_id, kwargs))

        edge_to_remove.append((t,f))

    G.remove_edges_from(edge_to_remove)

    for n in nodes_to_merge:
        G.remove_node(n)

    G.add_edges_from(edge_list)

    return  G

def update_network_node_data(G,new_column_id,new_values_dict):
    for n in G.nodes:
        G[n].update({new_column_id:new_values_dict[n]})

def update_network_edge_data(G,new_column_id,new_values_dict):
    for i,j in G.edges:
        G[i][j].update({new_column_id:new_values_dict[(i,j)]})