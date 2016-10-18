#!/usr/bin/env python

default_option = {"layout": 'grid'}
ALL_CYTOSCAPE_PRESET_LAYOUTS = ('grid','null','random','preset','circle','concentric','breadthfirst','cose')

def validate_config(config):
    #Todo
    pass


def reverse_gif(filename):
    """
    unused.
    taken from http://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
    """
    from PIL import Image, ImageSequence
#    from images2gif import writeGif
    from src.static.python.images2gif import writeGif
    import sys, os
    filename = sys.argv[1]
    im = Image.open(filename)
    original_duration = im.info['duration']
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    frames.reverse()

    writeGif("reverse_" + os.path.basename(filename), frames, duration=original_duration/1000.0, dither=0)

def make_gif_from_filepaths(output_filename, png_filepath_list, duration=2):
    from PIL import Image
#    from images2gif import writeGif
    from src.static.python import images2gif
    image_list = []

    for filepath in png_filepath_list:
        image_list.append(Image.open(filepath))


    images2gif.writeGif(output_filename, image_list, duration=duration)

    print("Done!")

def make_gif_from_png_base64(output_filename, png_b64_list, duration=2):
    #from images2gif import writeGif
    from src.static.python import images2gif

    image_list = list(map(b64toImage,png_b64_list))
    images2gif.writeGif(output_filename, image_list, duration=duration)
    print("Done!")

def make_gif_from_image_list(output_filename, image_list, duration=2):
#    from images2gif import writeGif
    from src.static.python import images2gif
    images2gif.writeGif(output_filename, image_list, duration=duration)

def graph_sequence_to_gif(output_filename, graph_list, visual_config=default_option, tmp_location=""):
    import uuid
#    from gif import make_gif
    # Todo : validate given layout


    temp_files_list = []
    for G in graph_list:
        temp_filename = tmp_location+ uuid.uuid4().hex
        networkx_to_cytoscape_html(temp_filename, G, visual_config)
        temp_files_list.append(temp_filename)

    png_images_bytearrays = html_to_png(temp_files_list,save=False)

    make_gif_from_png_base64(output_filename, png_images_bytearrays, duration=2)

    import os
    for temp_file in temp_files_list:
        os.remove(temp_file)


def render_html(file_location):
    """open a Firefox browser with the given graph, returns the selenium browser instance."""
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get("file://"+file_location)
    return browser


def b64toImage(base64_input):
    """
    Cast a base 64 encoded unicode string in input to a PIL Image instance.
    :param base64_input:
    :return: an Image instance from the PIL library
    """
    import io
    from PIL import Image
    import base64

    bytes = base64.b64decode(base64_input)
    return Image.open(io.BytesIO(bytes))


def save_png(base64_input,output_file):
    """

    :param base64: a base 64 encoded unicode string representing a png image
    :param output_file: the path where the image will be saved.
    """

    image = b64toImage(base64_input)
    image.save(output_file)

def html_to_png(filepaths, width=1280, height=720,save=False):
    """
    Takes in input one or a list of paths to html files of networks


    N.B. Common possible error :
            - (variable cy not found) can be caused by unvalidity of the source of the cytoscape.js in the html file.

    :param filepaths: can be one or a list of path to html network files. absolute and relative path are supported.
    :param width: the image width
    :param height: the image height
    :param save: if True, the generated png will be saved in the same directory then its html counterpart.
    :return: a list of png encoded as base 64 unicode strings
    """
    from selenium import webdriver
    from xvfbwrapper import Xvfb
    import os

    is_list = hasattr(filepaths, "__iter__")
    if not is_list:
        assert type(filepaths) is str
        filepaths = [filepaths]

    #Xvfb for headless mode
    xvfb = Xvfb(width=width, height=height)
    xvfb.start()

    browser = webdriver.Firefox()

    def cast_html_to_png(file_location):
        browser.get("file://"+file_location)
        print("file://"+file_location)
        b64 = browser.execute_script('return cy.png()')
        #cy.jpg()
        #cy.json()
        #index is always 22
        index = b64.index("base64,") + len("base64,")
        return b64[index:]

    abspath = os.getcwd()

    png_images = []
    for f in filepaths:
        if f[0] != '/':
            f = os.path.join(abspath,f)
        print("File : "+f)

        png_images.append(cast_html_to_png(f))

        if save :
            if len(f)>5 and f[-5:] == ".html":
                f = f[:-5]
            f += ".png"

            print(f)
            save_png(png_images[-1],f)

    browser.quit()
    xvfb.stop()
    return png_images

# Valid node shape : rectangle, roundrectangle, ellipse, triangle, pentagon, hexagon, heptagon, octagon, star, diamond, vee, rhomboid

##
## Options :
##  -- add callback options
##  -- replace this by cytoscape style sheets

def _generate_stylesheet_cytoscape(G, options):
    """


    Handles the preset layout and style options. For further information, see documentation.

    :param options : a dictionnary indicating the layout and style to apply.
    """
#    http: // js.cytoscape.org /  # cy.makeLayout

    if "shape" in options.keys():
        shape = options['shape']
    else :
        shape = "hexagon"

    node_size_option = ""
    if "node_size" in options.keys():
        from src.scripts import analytics
        opt = options["node_size"]
        if opt == "betweeness":
            analytics.compute_node_betweeness(G)
        elif opt == "connectivity":
            analytics.compute_node_eigenvect(G,"connectivity")
        elif opt == "closeness":
            analytics.compute_node_closeness(G)
        else :
            raise Exception("The option "+str(opt)+" for node size is unknowned.")

        node_size_option = """,
                'width':'data("""+opt+""")',
                'height':'data("""+opt+")'"

    node_style = """
        {selector: 'node',
         style: {"""+"""shape: '{shape}',
                'background-color': 'red'{node_size_option}
         """.format(shape=shape,node_size_option=node_size_option) + "}\n}"

    style = node_style

    if "edge_width" in options.keys():
        opt = options["edge_width"]
        if opt == "betweeness":
            analytics.compute_edge_betweeness(G)
        else :
            raise Exception("The option " + str(opt) + " for edge width is unknowned.")

        edge_style = """,
        {selector: 'edge',
        style : {"""
        + """'width': 'data({id})' """.format(id=opt) + "}\n}"
        style += edge_style


    if "background-opacity" in options.keys():
        extra_style = """,
        {
          selector: ':parent',
          style: {
            'background-opacity': {opacity}
          }
        }""".format(opacity=options["background-opacity"])

        style += extra_style

    return style


def _generate_layout_cytoscape(options):
    assert "layout" in options
    opt = options["layout"]
    assert opt in ALL_CYTOSCAPE_PRESET_LAYOUTS
    if opt == 'preset':
        raise NotImplementedError()


    return "{name: '"+opt+"'}"

def _generate_element_list_cytoscape(graph, options,verbose=False):
    node_id_list = graph.nodes()
    edges_id_list = graph.edges()

    if verbose :
        print('node_id_list : '+str(node_id_list))
        print('edge_id_list : '+str(edges_id_list))

    elements = ""
    for n in node_id_list:
        elements += "\n{ data: { id: '"+str(n)+"' } },"

    for u,v in edges_id_list:
        elements += """\n{
    data: {"""+"""
      id: '{source_id}{target_id}',
      source: '{source_id}',
      target: '{target_id}'\n""".format(source_id=u,target_id=v) +"}\n},"

    if len(elements) > 0:
        elements = elements[:-1]

    return elements

def networkx_to_cytoscape_html(output_filename, graph, options=default_option, verbose=False):
    """
    This functions takes in input a networkx graph and a dictionnary of options and creates a html file containing the graph rendered according to the given options and the cytoscape.js library (i.e. self-contained).

    option is a dictionnary in which the key 'layout' must be present.

    - For now, all generated graph are undirected.

    :param graph:
    :param output_filename:
    :param options:
    :param verbose: print extra details if true.
    :return:
    """

    style = _generate_stylesheet_cytoscape(graph, options)

    layout = _generate_layout_cytoscape(options)

    elements = _generate_element_list_cytoscape(graph, options,verbose)

    import os
    print(os.getcwd())
    cytoscape_library = open("./src/static/js/cytoscape.js-2.7.10/cytoscape.min.js",'r').read()

    # Set script path sur based on working directory?
    # src="../static/js/cytoscape.js-2.7.10/cytoscape.js"></script>

    html_template =  """<!doctype html>
<script>""" +cytoscape_library+ """</script><html>

<head>
    <title>Rendered Network</title>
</head>

<style>
    #cy {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0px;
        left: 0px;
    }
</style>
<body>
    <div id="cy"></div>
</body>
</html>
<script>
  var cy = cytoscape({
    container: document.getElementById('cy'),
    elements: ["""+elements+"""],
      style: ["""+style+"""],
      layout:["""+layout+"""]
  });
</script>
"""

    if verbose:
        print("Writing html network at "+str(output_filename))
    f = open(output_filename,'w')
    f.write(html_template)
    f.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='visual utils scripts')
    parser.add_argument('input', metavar='i', type=str,
                        help='The path to the network(s) in input. File(s) in input must be binary-writted pickled networkx instance(s).' )
    parser.add_argument('output', metavar='o', type=str,
                        help='The desired output location. Format has to be specified between .html, .png or .gif')
    parser.add_argument('configuration', metavar='c', type=str, default=None,
                        help='The path to the layout and style configuration json file.')

    args = parser.parse_args()
    print(args)

    config = args.configuration
    if config is None :
        config = default_option
    else :
        import json
        config = json.load(config)
        validate_config(config)




#    print args.accumulate(args.integers)
