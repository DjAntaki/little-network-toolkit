#!/usr/bin/env python

default_layout = {"shape":"hexagon"}
ALL_CYTOSCAPE_PRESET_LAYOUTS = ('grid','null','random','preset','circle','concentric','breadthfirst','cose','hexagon')

def reverse_gif(filename):
    """
    unused.
    taken from http://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
    """
    from PIL import Image, ImageSequence
#    from images2gif import writeGif
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

def graph_sequence_to_gif(output_filename, graph_list,layout=default_layout):
    import uuid
#    from gif import make_gif
    # Todo : validate given layout


    tmp_template = "tmp/"
    temp_files_list = []
    for G in graph_list:
        temp_filename = tmp_template+ uuid.uuid4().hex
        networkx_to_cytoscape_html(G,temp_filename,layout)
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
    browser.get(file_location)
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

def _generate_layout_cytoscape(options):
    """handles the preset options"""
#    http: // js.cytoscape.org /  # cy.makeLayout
    #Todo


    pass

def networkx_to_cytoscape_html(graph,output_filename,layout=default_layout,verbose=True):
    """
    Take in input a network

    For now, all generated graph are undirected.

    Some predefined layout are located in the visual_utils.py file.
    More to come.

    :param graph:
    :param output_filename:
    :param layout:
    :param verbose: print extra details if true.
    :return:
    """

    shape = layout['shape']
    assert shape in ALL_CYTOSCAPE_PRESET_LAYOUTS
    if shape == 'preset':
        raise NotImplementedError()

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

    style = """ shape: '{layout}',
        'background-color': 'red'
            """.format(layout=shape)
    cytoscape_library = open("../static/js/cytoscape.js-2.7.10",'r').read()

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
      style: [
    {
        selector: 'node',
        style: {
"""+style+"""
      }
    }]
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
                        help='The path to the network(s) in input. Format has to be specified between .csv, .nx, .html or .gif' )
    parser.add_argument('output', metavar='o', type=str,
                        help='The desired output location. Format has to be specified between .csv, .nx, .html or .gif')

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
#    print args.accumulate(args.integers)




#import subprocess
#subprocess.call(["python","/bin/webkit2png","http://bReNdAdIcKsOn.com"])

#subprocess.call(["python", "webkit2png.py", link])

#"--output "+out_filename

# https://pypi.python.org/pypi/xvfbwrapper/0.2.7
#http://blog.js.cytoscape.org/2016/05/24/getting-started/
#http://html2canvas.hertzen.com/examples.html
