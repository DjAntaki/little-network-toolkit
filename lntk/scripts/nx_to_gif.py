#!/usr/bin/env python
from lntk.visual_utils import default_option, validate_config, networkx_to_cytoscape_html, html_to_png, \
    make_gif_from_png_base64

def graph_sequence_to_gif(output_filename, graph_list, visual_config=default_option, duration=2, tmp_location=""):
    import uuid
#    from gif import make_gif
    # Todo : validate given layout
    validate_config(visual_config)

    temp_files_list = []
    for G in graph_list:
        temp_filename = tmp_location+ uuid.uuid4().hex
        networkx_to_cytoscape_html(temp_filename, G, visual_config)
        temp_files_list.append(temp_filename)

    png_images_bytearrays = html_to_png(temp_files_list,save=False)

    make_gif_from_png_base64(output_filename, png_images_bytearrays, duration=duration)

    import os
    for temp_file in temp_files_list:
        os.remove(temp_file)

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

    graph_sequence_to_gif(out,network_list,config)
