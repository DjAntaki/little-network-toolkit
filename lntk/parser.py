
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

    with open(node_csv_path,'r') as f:
        csv_reader = list(csv.reader(f))
        i=0
        if header is False:
            assert type(node_id_column) is int
        else :
            column_ids = csv_reader[0]
            i += 1
            if isinstance(node_id_column,str):
                node_id_column = column_ids.index(node_id_column)
            column_ids.pop(node_id_column)

        node_list = []
        for entry in csv_reader[i:]:
            n_id = entry.pop(node_id_column)

            if header and len(entry)>0:
                node_list.append((n_id,{i:j for i,j in zip(column_ids,entry)}))
            else :
                node_list.append((n_id,{}))
        return node_list

def parse_edges_csv(edge_csv_path, edge_id_column1=0, edge_id_column2=1, header=True):
    with open(edge_csv_path,'r') as f:
        csv_reader = list(csv.reader(f))

        i=0
        if header is False:
            assert type(edge_id_column1) is int
            assert type(edge_id_column2) is int
        else :
            column_ids = csv_reader[0]
            i += 1
            if isinstance(edge_id_column1,str):
                edge_id_column1 = column_ids.index(edge_id_column1)
            if isinstance(edge_id_column2, str):
                edge_id_column2 = column_ids.index(edge_id_column2)

        edge_list = []
        for entry in csv_reader[i:]:
            if edge_id_column1 < edge_id_column2:
                edge_id2 = entry.pop(edge_id_column2)
                edge_id1 = entry.pop(edge_id_column1)
            elif edge_id_column1 == edge_id_column2 :
                edge_id2 = entry.pop(edge_id_column2)
                edge_id1 = edge_id2
            else:
                edge_id1 = entry.pop(edge_id_column1)
                edge_id2 = entry.pop(edge_id_column2)

            if header and len(entry) > 0:
                #Todo : add edges attributes
                edge_list.append((edge_id1,edge_id2))
            else :
                edge_list.append((edge_id1,edge_id2))

        return edge_list

def csv_to_networkx(node_csv, edge_csv,node_id=0,edge_id1=0,edge_id2=1, header=True, verbose=False):
    """

    Everything is casted as a string.

    :param node_csv:
    :param edge_csv:
    :param node_id:
    :param edge_id1:
    :param edge_id2:
    :param header:
    :param verbose:
    :return:
    """

    if verbose:
        print("Parsing node csv...")
    node_list = parse_nodes_csv(node_csv,node_id,header)
    if verbose:
        print("Parsing edges csv...")
    edge_list = parse_edges_csv(edge_csv,edge_id1,edge_id2,header)

    G = nx.Graph()
    G.add_edges_from(edge_list)
    G.add_nodes_from(node_list)
    return G

def networkx_to_csv(G,node_csv_path,edge_csv_path,header=True):
    """
    Generate two csv from a networkx graph. The first one represents a list of nodes while the second represents a list of edges.

    :param G: a networkx graph
    :param node_csv_path: the path to the node csv output location
    :param edge_csv_path: the path to the edge csv output location
    :param header: If True, the generated csv will have a header.
    """
    edge_list = []
    edge_header_items = ["Id1","Id2"]
    all_keys_edges = set()
    for edge_id1, edge_id2 in G.edges():
        data = G[edge_id1][edge_id2]
        edge_list.append((edge_id1,edge_id2,data))
        for k in data.keys():
            all_keys_edges.add(k)

    edge_header_items += list(sorted(all_keys_edges))

    node_list = []
    all_keys_nodes = set()
    for node_id in G.nodes():
        data = G[node_id]
        node_list.append((node_id,data))
        for k in data.keys():
            all_keys_nodes.add(k)

    for n in node_list:
        all_keys_nodes.remove(n[0])

    node_header_items = ["Id"]
    node_header_items += list(sorted(all_keys_nodes))


    #Writing the edge list in a csv
    f_edges = open(edge_csv_path,'w')
    if header :
        f_edges.write(", ".join(edge_header_items)+"\n")

    for edge_id1,edge_id2,data in edge_list:
        entry = [str(edge_id1),str(edge_id2)]
        if header :
            for h in edge_header_items[2:]:
                if h in data.keys():
                    entry.append(data[h])
                else :
                    entry.append("")
        f_edges.write(",".join(entry) + "\n")

    f_edges.close()

    #Writing node list in csv
    f_nodes = open(node_csv_path,'w')
    if header :
        f_nodes.write(",".join(node_header_items)+"\n")
    for node_id,data in node_list:
        entry = [str(node_id)]
        if header :
            for h in node_header_items[1:]:
                print(h)
                if h in data.keys() and not h in node_list:
                    entry.append(data[h])
                else :
                    entry.append("")
        f_nodes.write(",".join(entry) + "\n")
    f_nodes.close()



