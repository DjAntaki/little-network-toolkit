# Little Network Toolkit (LNTk)
***work in progress***

A collection of scripts to import, save, manipulate and render undirected graph. Feel free to use.

## Content

- Parse csv to networkx
- Parse networkx graph to html file using layout functionnality of cytoscape 2.7.10
- Save that networkx graph to png
- Can create a gif from a list of networkx graph

## Documentation

Documentation has been generated with sphinx. A compiled version of the documentation is included under the "doc/_build/" directory of the repository.

## Dependencies

### Programs

#### Xvfb

    sudo apt-get install xvfb

#### Geckodriver

    npm install geckodriver

Alternatively, geckodriver can be downloaded at https://github.com/mozilla/geckodriver/releases/. If npm or nodejs is not installed on your machine use command
    sudo apt-get install npm nodejs

Then, make sure you that geckodriver is in your path. If it is not, look into nodejs "node_modules" directory and use the command :
    export PATH=$PATH:/path/to/nodejs/directory/node_modules/geckodriver/


### Python libraries

These can be installed with the command *python setup.py build*

- Networkx
- Selenium
- Xvfbwrapper
- Pillow

### Included libraries

The source code of the following libraries are included in the directory "static" of the source code.

- cytoscape.js 2.7.19
- images2gif (https://pypi.python.org/pypi/images2gif)

## Unittest

Unittest are done with the nose library. To run them, use command

    nose lntk/tests

## Details

###

Networkx graph are saved with *pickle* and with the extension. They can be import in the following way :

    import pickle
    graph = pickle.load(open("./mygraph",'rb'))

### CSV to networkx

Two csv are required to get a networkx graph. The first provided csv defines the nodes while the second defines the edges. By default, the first columns of the node csv is interpreted as node id and the first and second columns of the edge csv are interpreted respectively as the source and target of the edge. It is not possible to change that behavior using the command line interface.



By default, it is assumed that first line of the csv is a header containning the columns ids. If it is not the case, the flag --header false can be passed to the command line util.

The created graph is defined as




- CSVs can have extra data columns which will transfer to networkx node and edge attributes

## Usages

### Command line use

Here is listed all the command line use cases.

#### Parse csv to networkx

    lntk-csvparser <node_list_csv> <edge_list_csv> <output_networkx_file> [--header]

#### Parse networkx to csv

    lntk-parser -i <input_file>.nx -o <output_node_list>.csv <output_edge_list>.csv [--header]

#### networkx to png

    lntk-viz -i <networkx_input_file>  -o <output_file>.png [-c display_config]

#### List of networkx graph to gif

    lntk-viz -i <networkx_file1> <networkx_file2> <networkx_file3> -o <output_file>.gif [-l layout_preset] [-c display_config]

### Display configuration

The display configuration is a json that defines layout and style of the graph. Here is a list of all interpretable key and the values they can take.

- "layout":('grid','null','random','circle','concentric','breadthfirst','cose','hexagon')
- "node_size":["betweeness","closeness","connectivity"]
- "edge_width":["betweeness"]
- "shape":["rectangle", "roundrectangle", "ellipse", "triangle", "pentagon", "hexagon", "heptagon", "octagon", "star", "diamond", "vee", "rhomboid"]}

In that sense, the following is a valid display configuration :

    {'layout':'cose',
     'node_size':'betweeness'}

### Library use

The scripts can be accessed in an python interpreter with the command *import LNTk*. This allows access to all scripts, including the network manipulation scripts which aren't accessible from the command line.

To open a graph in a browser :

    import LNTk
    LNTk.visual_utils.render_html(graph)
