import unittest
from selenium import webdriver
from xvfbwrapper import Xvfb
from src.scripts import visual_utils
from src.datasets.generated import get_gnp_series
import os
#from nose import with_setup


class TestHTML(unittest.TestCase):
    def setUp(self):
        self.graphs = get_gnp_series()

    def tearDown(self):
        os.remove("test.html")

    def test_networkx_to_html(self):
        visual_utils.networkx_to_cytoscape_html(self.graphs[0], output_filename="test.html")

    def test_networkx_to_png(self):
        visual_utils.networkx_to_cytoscape_html(self.graphs[0], output_filename="test.html")
        visual_utils.html_to_png("test.html")

class TestGif(unittest.TestCase):
    def setUp(self):
        from src.datasets.generated import get_gnp_series
        self.graphs = get_gnp_series()

    def tearDown(self):
        #Check if it has been created first?
        os.remove("tmp/test.gif")

    def test_make_gif(self):
        visual_utils.graph_sequence_to_gif("test.gif", self.graphs)


class TestMultipleLayouts(unittest.TestCase):
    def __init__(self):
        from src.scripts.visual_utils import ALL_CYTOSCAPE_PRESET_LAYOUTS as all_layouts

        all_layouts.remove('preset')
        for layout in all_layouts:
            self.set_layout_case(layout)

    def set_layout_case(self,layout):
        def test_layout(self):
            pass
        setattr(self, "test_" + layout,test_layout)

    def setUp(self):
        pass

    def test_preset_case(self):
        pass

class TestRenderer(unittest.TestCase):
    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_render_html(self):
        #    file_location = 'file:///home/ntak/Documents/mcgill/comp767/assignment5/little-network-toolkit/src/examples/network_example.html'
        print(os.getcwd())
        file_location = "file:///home/kameha/Documents/mcgill_stuff/comp767/assignment5/little-network-toolkit/src/nosetests/test_data/test.html"
        browser = visual_utils.render_html(file_location)



            #html_to_png(filepaths, width=1280, height=720)
#save_png(bytearray, output_file)
#render_html(file_location)