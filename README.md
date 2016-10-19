# little-network-toolkit (lntk)

A collection of scripts to import, save, manipulate and render undirected graph.

## Content

- Parse csv to networkx and networkx to csv
- Parse networkx graph to html file using layout functionalities from cytoscape 2.7.10
- Save a networkx graph to png
- Can create a gif from a list of networkx graph

## Documentation

Documentation has been generated with *Sphinx*. A html compiled version of the documentation is included under the "doc/_build/" directory of the repository.

## Installation

### Prerequisite programs list

Here is a list of non-python dependencies for the scripts and the way to install them on Ubuntu 16.04

#### Xvfb

    sudo apt-get install xvfb

#### Geckodriver

Before installing geckodriver, you must have npm and nodejs-legacy installed on your machine. If it is not the case, use the command :

    sudo apt-get install npm nodejs-legacy

Then, to install geckodriver

    npm install geckodriver

Alternatively, geckodriver can be downloaded at https://github.com/mozilla/geckodriver/releases/.

Then, make sure you that geckodriver is in your path. If it is not, add the following command to your ~/.bashrc file :

    export PATH=$PATH:/path_to_nodejs_directory/node_modules/geckodriver/


### Installation with pip

To install the program with pip python package manager, enter the following commands.

    cd little-network-toolkit
    pip install -e .

Here is a list of the libraries that will be installed :

- Networkx
- Selenium
- Xvfbwrapper
- Pillow

### Add command line options

To have the command line interface, we need to add the scripts in the 'usr/local/bin' directory. To do so, run the following commands from this projects main folder.

    sudo su add_to_path.sh

Doing this should add the commands "lntk-csv_to_nx", "lntk_nx_to_csv", "lntk-renderer" and "lntk-nx_to_gif" to your bash shell.

### Included libraries

The source code of the following libraries are included in the directory "static" of the source code. Thus, nothing is required for installation.

- cytoscape.js 2.7.19
- images2gif (https://pypi.python.org/pypi/images2gif)

## Unittest

Unittest are done with the nose library. To run them, use command

    nosetests lntk/tests

## Some considerations

### Networkx graph instance loading

Networkx graph are saved with *pickle*. They can be import in the following way :

    import pickle
    graph = pickle.load(open("./mygraph",'rb'))

### Display configuration

The display configuration is a json that defines layout and style of the graph. Here is a list of all interpretable keys and the values they can take. The display configuration must have an entry under the key "layout".

- "layout":('grid','null','random','circle','concentric','breadthfirst','cose','hexagon')
- "node_size":["betweeness","closeness","connectivity"]
- "edge_width":["betweeness"]
- "shape":["rectangle", "roundrectangle", "ellipse", "triangle", "pentagon", "hexagon", "heptagon", "octagon", "star", "diamond", "vee", "rhomboid"]}

In that sense, the following is a valid display configuration :

    {"layout":"cose",
     "node_size":"connectivity",
     "edge_size":"betweeness"}

## Usages

### Library use

The scripts can be accessed in an python interpreter with the command *import lntk*. This allows access to all scripts, including the network manipulation scripts which aren't accessible from the command line.

For example, to open a graph in a browser :

    import lntk
    lntk.visual_utils.render_html(graph)


### Command line use

Here is listed all the command line use cases. All of those command have their function equivalent in the librairy

#### Parse csv to networkx

    lntk-csv_to_nx <input_node_list_csv> <input_edge_list_csv> <output_networkx_file> [--no-header]

Two CSVs are required to get a networkx graph. The first provided csv defines the nodes while the second defines the edges. By default, the first columns of the node csv is interpreted as node id and the first and second columns of the edge csv are interpreted respectively as the source and target of the edge. It is not possible to change that behavior using the command line interface.

By default, it is assumed that first line of the csv is a header containning the columns ids. If it is not the case, the flag --no-header can be passed as argument.

N.B. If a header is provided, CSVs can have extra data columns which will transfer to networkx node and edge attributes

#### Parse networkx to csv

    lntk-nx_to_csv <networkx_input_file> <output_node_list_csv> <output_edge_list_csv> [--no-header]

By default, a header is generated. Use the --no-header flag to avoid generating a header.

#### networkx to html

    lntk-renderer <networkx_input_file> <html_output_path> html <display_config_path> 

#### networkx to png

    lntk-renderer <networkx_input_file> <png_output_path> png <display_config_path>

#### List of networkx graph to gif

    lntk-nx_to_gif <networkx_file1> <networkx_file2> ... <networkx_file99> <gif_output_path> <display_config_path>
