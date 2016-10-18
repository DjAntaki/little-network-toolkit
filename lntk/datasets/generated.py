import networkx as nx



def get_gnp_series(l=5, n=20, p=0.5):
    """
    This function returns a series of graph with a fixed number of nodes. At each step, we generate a random graph and add the previous graph edges.

    :param l: the number of graph to return
    :param p: the probability of an edge between a node and one of its child
    :param n: the number of nodes

    :return: a sequence of graph
    """
    graph_sequence = []
    last_graph = None
    for k in range(l):

        graph = nx.gnp_random_graph(n,p)

        if not last_graph is None:
            for u,v in last_graph.edges():
                graph.add_edge(u,v)
        graph_sequence.append(graph)
        last_graph = graph

    return graph_sequence

if __name__ == "__main__":
    for g in get_gnp_series():
        print(g)
        for u,v in g.edges():
            print(u,v)