# little-network-toolkit (LNTk)
***work in progress***

A bunch of scripts b to import, save, manipulate and render undirected graph. Feel free to use.

## Dependencies

### Programs

- Xvfb


- Firefox
- Geckodriver  : https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-arm7hf.tar.gz
### Python libraries

These can be installed with the command *python setup.py build*

- Networkx
- Selenium
- Xvfbwrapper

## Content

- Parse csv to networkx
- Parse networkx to (undirected) html file using preset layout of cytoscape 2.7.10
- Save that networkx graph to *png*
- Can create a gif from a list of networkx graph

## Details

### .nx

Networkx graph are saved with *pickle* and with the extension ".nx". They can be import in the following way :

    import pickle
    graph = pickle.load("mygraph.nx")

### CSV to networkx

Two csv are required to get a networkx graph. The first provided csv defines the nodes. Its first columns is

By default, it is assumed that first line of the csv is a header containning the columns ids. If it is not the case, the flag --noheader can be passed to the command line util.

 The created graph is defined as




- CSVs can have extra data columns which will transfer to networkx node and edge attributes

## Usages

### Command line use

Here is listed all the command line use cases.

#### Parse csv to networkx

    lntk-parser -i <node_list>.csv <edge_list>.csv -o <output_file>.nx [--header]

#### Parse networkx to csv

    lntk-parser -i <input_file>.nx -o <output_node_list>.csv <output_edge_list>.csv [--header]

#### networkx to png

    lntk-viz -i <networkx_input_file>  -o <output_file>.png [-c display_config]

#### List of networkx graph to gif

    lntk-viz -i <networkx_file1> <networkx_file2> <networkx_file3> -o <output_file>.gif [-l layout_preset] [-c display_config]

### Display configuration

The display configuration is a json that defines layout and style of

Layout and style configuration

- preset layouts are : ('grid','null','random','preset','circle','concentric','breadthfirst','cose','hexagon')
- style presets are : V:node_size

### Library use

The scripts can be accessed in an python interpreter with the *import LNTk*. This allows access to all scripts, including the network manipulation scripts which aren't accessible from the command line.

To open a graph in a browser :

    import LNTk

    LNTk.visual_utils.render_html()
