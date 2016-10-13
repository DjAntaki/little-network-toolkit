# little-network-toolkit (LNTk)
A bunch of script to use. Feel free to use.

## Dependencies

### Programs

There programs can be found using the *apt-get* command or the equivalent on your distribution.

- Xvfb

### Python

These are can be installed with the command *python setup.py*

- Networkx
- Selenium
- Xvfbwrapper

## Content

- Parse csv to networkx
- Parse networkx to (undirected) html file using preset layout of cytoscape 2.7.10
- Save that networkx graph to *png*
- Can create a gif from a list of networkx graph

## Details

- Networkx graph are saved with pickle and with the extension ".nx".
- CSVs can have extra data columns which will transfer to networkx node and edge attributes
-

## Usages

### Command line use

Here is listed all the command line possible use cases.

#### Parse csv to networkx

    lntk -i <node_list>.csv <edge_list>.csv -o <output_file>.nx

#### Parse networkx to csv

    lntk -i <input_file>.nx -o <output_node_list>.csv <output_edge_list>.csv

#### csv to png

    lntk -i <node_list>.csv <edge_list>.csv  -o <output_file>.png [-l layout_preset] [-s style_preset]

#### networkx to png

    lntk -i <input_file>.nx  -o <output_file>.png [-l layout_preset] [-s style_preset]

#### List of networkx graph to gif

    lntk -i <network1>.nx <network2>.nx <network3>.nx -o <output_file>.gif [-l layout_preset] [-s style_preset]

### Available layout and style preset

- preset layouts are : ('grid','null','random','preset','circle','concentric','breadthfirst','cose','hexagon')
- style presets are :

### Library use

The scripts can be accessed in an python interpreter with the *import LNTk*. This allows access to all scripts, including the network manipulation scripts which aren't accessible from the command line.

To open a graph in a browser :

    import LNTk

    LNTk.visual_utils.render_html()
