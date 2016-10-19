import unittest
#from selenium import webdriver
#from xvfbwrapper import Xvfb
from copy import deepcopy
from PIL.Image import Image
from lntk import visual_utils
from lntk.datasets.generated import get_gnp_series
import networkx as nx
import os
#from nose import with_setup

def teardown_remove_files(filepaths):
    if hasattr(filepaths,"__iter__"):
        for f in filepaths:
            if os.path.isfile(f):
                os.remove(f)
            else:
                raise AssertionError("No file at "+f)

class TestHTML(unittest.TestCase):
    def setUp(self):
        self.graphs = get_gnp_series()
        self.tmp_root = os.getcwd() + "/lntk/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        teardown_remove_files(self.tmp_root+"test.html")

    def test_networkx_to_html(self):
        visual_utils.networkx_to_cytoscape_html(self.tmp_root+"test.html", self.graphs[0])

class TestNXtoPNG(unittest.TestCase):
    def setUp(self):
        self.graphs = get_gnp_series()
        self.tmp_root = os.getcwd() + "/lntk/tests/tmp/"
#        self.tmp_root = "src/tests/tmp/"

    def test_networkx_to_png(self):
        visual_utils.networkx_to_cytoscape_html(self.tmp_root+"test.html",self.graphs[0])
        b64png = visual_utils.html_to_png(self.tmp_root+"test.html",save=True)
        self.assertTrue(len(b64png)==1)
        im = visual_utils.b64toImage(b64png[0])
        from PIL.Image import Image
        self.assertTrue(isinstance(im,Image))
        teardown_remove_files([self.tmp_root + i for i in ("test.html", "test.png")])

    def test_layouts(self):
        from lntk.visual_utils import ALL_CYTOSCAPE_PRESET_LAYOUTS as all_layouts, default_option as defopt
        all_layouts = list(all_layouts)
        all_layouts.remove('preset')
        for layout in all_layouts:
            defopt['layout'] = layout
            visual_utils.networkx_to_cytoscape_html(self.tmp_root+"test.html",self.graphs[0],defopt)
            b64png = visual_utils.html_to_png(self.tmp_root+"test.html",save=False)
            self.assertTrue(len(b64png)==1)
            im = visual_utils.b64toImage(b64png[0])
            self.assertTrue(isinstance(im,Image))

        teardown_remove_files([self.tmp_root+"test.html"])

    def test_valid_options(self):
      #  return
        defopt = visual_utils.default_option
        options_to_test = {"node_size":["betweeness","closeness","connectivity"],"edge_width":["betweeness"],"shape":["rectangle",]}
        #let's not make the test long for nothing

      # "roundrectangle", "ellipse", "triangle", "pentagon", "hexagon", "heptagon", "octagon", "star", "diamond", "vee", "rhomboid"]}
        for key,values in options_to_test.items():
            for value in values :
                print("testing option "+str(key)+" with value "+str(value))
                opt = deepcopy(defopt)
                opt[key] = value
                visual_utils.networkx_to_cytoscape_html(self.tmp_root+"test.html",self.graphs[0],opt)
                b64png = visual_utils.html_to_png(self.tmp_root+"test.html",save=False)
                self.assertTrue(len(b64png)==1)
                im = visual_utils.b64toImage(b64png[0])
                self.assertTrue(isinstance(im,Image))

    def test_invalid_options(self):

        invalid_inputs = {'layout':'qwe', 'node_size':'qwe','edge_width':'qwe',"shape":'qwe'}
        defopt = visual_utils.default_option

        for key, value in invalid_inputs.items():
            opt = deepcopy(defopt)
            opt[key] = value
            self.assertRaises(AssertionError,visual_utils.networkx_to_cytoscape_html,self.tmp_root + "test.html", self.graphs[0], opt)


class TestGif(unittest.TestCase):
    def setUp(self):
        from lntk.datasets.generated import get_gnp_series
        self.graphs = get_gnp_series()
        self.tmp_root = os.getcwd()+"/lntk/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        teardown_remove_files(self.tmp_root+"test.gif")

    def test_make_gif(self):
        visual_utils.graph_sequence_to_gif("lntk/tests/tmp/test.gif", self.graphs, tmp_location=self.tmp_root)


# class TestRenderer(unittest.TestCase):
#     def test_render_html(self):
#         print(os.getcwd())
#         xvfb = Xvfb(width=1280, height=720)
#         xvfb.start()
#         file_location = "./src/nosetests/test_data/test.html"
#         browser = visual_utils.render_html(file_location)
#         browser.quit()
#         xvfb.stop()
