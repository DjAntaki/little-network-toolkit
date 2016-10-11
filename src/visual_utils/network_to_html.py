


def networkx_to_cytoscape_html(graph,output_filename,shape="hexagon"):

    assert shape in ['hexagon','circle'] #Todo : complete this

    node_id_list = graph.nodes()
    print('node_id_list',node_id_list)
    edges_id_list = graph.edges()

    elements = ""
    for n in node_id_list:
        elements += "\n{ data: { id: '"+str(n)+"' } },"

    for u,v in edges_id_list:
        elements += """\n{
            data: {\n"""+"""
              id: '{source_id}{target_id}',
              source: '{source_id}',
              target: '{target_id}'\n""".format(source_id=u,target_id=v) +"}\n},"

    if len(elements) > 0:
        elements = elements[:-1]

    style = """
                shape: '{layout}',
                'background-color': 'red'
            """.format(layout=shape)

#   print
    html_template =  """
        <!doctype html>

        <html>

        <head>
            <title>Tutorial 1: Getting Started</title>
            <script src="../static/js/cytoscape.js-2.7.10/cytoscape.js"></script>
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
        </body>
        </html>
        """

    f = open(output_filename,'w')
    f.write(html_template)

#import subprocess
#subprocess.call(["python","/bin/webkit2png","http://bReNdAdIcKsOn.com"])

#subprocess.call(["python", "webkit2png.py", link])

#"--output "+out_filename

# https://pypi.python.org/pypi/xvfbwrapper/0.2.7
#http://blog.js.cytoscape.org/2016/05/24/getting-started/
#http://html2canvas.hertzen.com/examples.html


def qwe():
    from xvfbwrapper import Xvfb
    vdisplay = Xvfb(width=1280, height=740, colordepth=16)
    vdisplay.start()

    # launch stuff inside
    # virtual display here.

    vdisplay.stop()

if __name__ == "__main__":
    from src.datasets.generated import get_gnp_series
    graphs = get_gnp_series()
    networkx_to_cytoscape_html(graphs[0], output_filename="test.html")