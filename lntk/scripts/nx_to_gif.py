#!/usr/bin/env python
from lntk.visual_utils import default_option, validate_config, graph_sequence_to_gif

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='LNTk networkx to gif')
    parser.add_argument('inputs', metavar='i', type=str, nargs='+',
                        help='The path to the network(s) in input. File(s) in input must be binary-writted pickled networkx instance(s).')
    parser.add_argument('output', metavar='o', type=str,
                        help='The desired output location.')
    parser.add_argument('configuration', metavar='c', type=str, default=None, help='The path to the layout and style configuration json file.')

    args = parser.parse_args()
  #  print(args)

    inp, out = args.input, args.output
    config = args.configuration

    network_list = []
    for i in inp:
        import pickle
        network = pickle.load(open(i,'rb'))
        network_list.append(network)

    if config is None :
        config = default_option
    else :
        import json
        config = json.load(config)
        validate_config(config)

    graph_sequence_to_gif(out, network_list, config)
