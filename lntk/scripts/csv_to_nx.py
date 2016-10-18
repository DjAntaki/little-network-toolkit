from lntk.parser import csv_to_networkx

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description='lntk-csvparser')
    parser.add_argument('input', metavar='i', type=str, nargs=2,
                        help='The path to two csv must be given. The first one is the node list and the second is the edge list.' )
    parser.add_argument('output', metavar='o', type=str,
                        help='The desired output location. Will save a pickled networkx graph.')
    parser.add_argument('--header',type=bool, default=True,
                        help="Boolean value representing the presence or absence of a header in the csv. Default is True.")


    args = parser.parse_args()
    print(args)
    node_list_csv, edge_list_csv = args.input
    out = args.output
    header = args.header

    netx = csv_to_networkx(node_list_csv, edge_list_csv,header=header)

    import pickle
    pickle.dump(netx,open(out,'wb'))

