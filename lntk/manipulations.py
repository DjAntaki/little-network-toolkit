
import networkx as nx

def merge_nodes(G, nodes_to_merge, new_node_id):
    """
    Merges a list of nodes in a graph

    :param G: a networkx graph
    :param nodes_to_merge: a list of node ids
    :param new_node_id: an id for the new node
    :return:
    """
    print('a')
    G.add_node(new_node_id)

    edge_list = []
    edge_to_remove = []
    for t,f in G.edges():

        first = False
        if t in nodes_to_merge:
            first = True
        if f in nodes_to_merge:
            if first :
                print('remove',t,f)
                kwargs = G[t][f]
                edge_list.append((new_node_id,new_node_id,kwargs))
                edge_to_remove.append((t, f))
                continue
        elif not first :
            print('do nothing', t, f)
            continue

        kwargs = G[t][f]

        if first :
            print('remove', t, f)
            edge_list.append((new_node_id, f, kwargs))
        else :
            print('remove', t, f)
            edge_list.append((t, new_node_id, kwargs))

        edge_to_remove.append((t,f))

    G.remove_edges_from(edge_to_remove)

    for n in nodes_to_merge:
        G.remove_node(n)

    G.add_edges_from(edge_list)

    return  G

def update_network_node_data(G,new_column_id,new_values_dict):
    #nx.set_node_attributes(G,new_column_id,new_values_dict)
    #return
    print(new_values_dict)
    print(G.nodes())
    for n in G.nodes():
        G.add_node(n,{new_column_id: new_values_dict[n]})
#        G[n].update({new_column_id:new_values_dict[n]})

def update_network_edge_data(G,new_column_id,new_values_dict):
    for i,j in G.edges():
        G[i][j].update({new_column_id:new_values_dict[(i,j)]})