import unittest
from selenium import webdriver
from xvfbwrapper import Xvfb
from src.scripts import visual_utils
from src.datasets.generated import get_gnp_series
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
        self.tmp_root = os.getcwd() + "/src/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        print(os.getcwd())
        teardown_remove_files(self.tmp_root+"test.html")

    def test_networkx_to_html(self):
        visual_utils.networkx_to_cytoscape_html(self.graphs[0], output_filename=self.tmp_root+"test.html")

class TestHTMLtoPNG(unittest.TestCase):
    def setUp(self):
        self.graphs = get_gnp_series()
        self.tmp_root = os.getcwd() + "/src/tests/tmp/"
#        self.tmp_root = "src/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        print(os.getcwd())
        teardown_remove_files([self.tmp_root+i for i in ("test.html","test.png")])

    def test_networkx_to_png(self):
        visual_utils.networkx_to_cytoscape_html(self.graphs[0], output_filename=self.tmp_root+"test.html")
        b64png = visual_utils.html_to_png(self.tmp_root+"test.html",save=True)
        self.assertTrue(len(b64png)==1)
        im = visual_utils.b64toImage(b64png[0])
        from PIL.Image import Image
        self.assertTrue(isinstance(im,Image))


class TestGif(unittest.TestCase):
    def setUp(self):
        from src.datasets.generated import get_gnp_series
        self.graphs = get_gnp_series()
        self.tmp_root = "src/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        print(os.getcwd())
        teardown_remove_files(self.tmp_root+"test.gif")

    def test_make_gif(self):
        visual_utils.graph_sequence_to_gif("src/tests/tmp/test.gif", self.graphs,tmp_location=self.tmp_root)


class TestMultipleLayouts(unittest.TestCase):
    @staticmethod
    def setUpClass():
        from src.scripts.visual_utils import ALL_CYTOSCAPE_PRESET_LAYOUTS as all_layouts

        all_layouts = list(all_layouts)
        all_layouts.remove('preset')

        def set_layout_case(layout):
            def test_layout(self):
                print("test_layout",self)
                assert False
                pass
            setattr(TestMultipleLayouts, "test_" + layout,test_layout)

        for layout in all_layouts:
            set_layout_case(layout)
            pass

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