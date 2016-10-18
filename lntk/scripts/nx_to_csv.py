#!/usr/bin/env python
from lntk.parser import networkx_to_csv

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='lntk_nx-to-csv')
    parser.add_argument('input', metavar='i', type=str,
                        help='The path to a pickled networkx graph.' )
    parser.add_argument('output', metavar='o', type=str, nargs=2,
                        help='The desired outputs location. Will save two csv. The first one is the node list and the second is the edge list. ')

    args = parser.parse_args()
    print(args)
    inp = args.input
    node_list_csv, edge_list_csv = args.output
    header = args.header

    import pickle
    network = pickle.load(open(inp,'rb'))
    networkx_to_csv(network,node_list_csv,edge_list_csv)

