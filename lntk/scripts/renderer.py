#!/usr/bin/env python
from lntk import visual_utils as vu

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='LNTk visual utilities scripts')
    parser.add_argument('input', metavar='i', type=str,
                        help='The path to the network in input. File in input must be binary-writted pickled networkx instance.' )
    parser.add_argument('output', metavar='o', type=str,
                        help='The desired output location.')
    parser.add_argument('output_type',metavar='t',type=str ,default='png',
                        help="The desired output type. Either 'html' or 'png'.")

    parser.add_argument('configuration', metavar='c', type=str, default=None,nargs='?', help='The path to the layout and style configuration json file.')

    args = parser.parse_args()
#    print(args)

    inp, out = args.input, args.output
    config, out_type = args.configuration,  args.output_type

    import pickle
    network = pickle.load(open(inp,'rb'))

    if config is None :
        config = vu.default_option
    else :
        import json
        config = json.load(open(config,'r'))
        #I'm not sure its a great way to deal with encoding but it seems to do the trick.
        config = {str(i): str(j) for i,j in config.items()}
        vu.validate_config(config)

    if out_type == "png":
        import uuid
        temp_file = "temp_"+str(uuid.uuid4())
        vu.networkx_to_cytoscape_html(temp_file, network, options=config)
        b64input = vu.html_to_png(temp_file, width=1280, height=720, save=False)
        vu.save_png(b64input, out)
    elif out_type == "html":
        vu.networkx_to_cytoscape_html(out, network, options=config)
    else :
        raise Exception("Unrecognized output format: "+str(out_type))

