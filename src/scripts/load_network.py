
import csv
import networkx as nx

def parse_nodes_csv(node_csv_path, node_id_column=0, header=True):
    """

    If no header is present, only the ids will be retrieve. If a header is present, every columns except the id columns
    will be

    :param node_csv_path:
    :param node_id_column:
    :param header:
    :return:
    """

    if header is False:
        assert type(node_id_column) is int

    #Todo
    csv.reader(node_csv_path)

def parse_edges_csv(edge_csv_path, edge_id_column1=0, edge_id_column2=1, header=True):
    with open(edge_csv_path,'r') as f:
        csv_reader = csv.reader(f)

        i=0
        if header is False:
            assert type(edge_id_column1) is int
            assert type(edge_id_column2) is int
        else :
            column_ids = csv_reader[0] #or something
            i += 1
            if isinstance(edge_id_column1,str):
                edge_id_column1 = column_ids.index(edge_id_column1)
            if isinstance(edge_id_column2, str):
                edge_id_column2 = column_ids.index(edge_id_column2)

        edge_list = []
        for entry in csv_reader[i:]:
            if edge_id_column1 < edge_id_column2:
                edgeid2 = entry.pop(edge_id_column2)
                edgeid1 = entry.pop(edge_id_column1)
            elif edge_id_column1 == edge_id_column2 :
                edgeid2 = entry.pop(edge_id_column2)
                edgeid1 = edgeid2
            else:
                edgeid1 = entry.pop(edge_id_column1)
                edgeid2 = entry.pop(edge_id_column2)

            if header and len(entry) > 0:
                #Todo : add misc arguments
                edge_list.append((edge_id_column1,edge_id_column2))
            else :
                edge_list.append((edge_id_column1,edge_id_column2))

        return edge_list

def csv_to_networkx(node_csv, edge_csv,node_id=0,edge_id1=0,edge_id2=1, header=True, verbose=False):

    if verbose:
        print("Parsing node csv...")
    node_list = parse_nodes_csv(node_csv,node_id)
    if verbose:
        print("Parsing edges csv...")
    edge_list = parse_edges_csv(edge_csv,edge_id1,edge_id2)

    G = nx.Graph()
    G.add_edges_from(edge_list)
    G.add_nodes_from(node_list)
    return G
    #Assert all edges id are in nodes_id?
    pass

def dictionnary_to_networkx(dic):
    """ """

def networkx_to_csv(G,node_csv_path,edge_csv_path):

    edge_list = []
    header_items = []
    for edge_id1, edge_id2 in G.edge_list():
        data = G[edge_id1][edge_id2]
        edge_list.append((edge_id1,edge_id2,data))

    #Writing the edge list in a csv




    pass




if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')

    args = parser.parse_args()
    print args.accumulate(args.integers)


