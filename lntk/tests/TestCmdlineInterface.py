import networkx.algorithms.isomorphism as iso
import os
import pickle
import subprocess as su
import unittest
import networkx as nx
import json
from PIL import Image
ImageClass = Image.Image
from lntk import visual_utils
from copy import deepcopy
from lntk.visual_utils import ALL_CYTOSCAPE_PRESET_LAYOUTS, default_option as defopt

def teardown_remove_files(filepaths):
    if hasattr(filepaths,"__iter__"):
        for f in filepaths:
            if os.path.isfile(f):
                os.remove(f)

class CSV_parse_test(unittest.TestCase):
    def setUp(self):
        self.G = nx.generators.classic.complete_graph(10)

    def tearDown(self):
        teardown_remove_files(["test_node_csv","test_edges_csv","test_out.nx"])

    def test_cmdline_back_and_forth(self):
        pickle.dump(self.G,open("test_out.nx",'wb'))

        su.check_call(["lntk-nx_to_csv", "test_out.nx","test_nodes_csv", "test_edges_csv"])

        su.check_call(["lntk-csv_to_nx","test_nodes_csv","test_edges_csv", "test_out.nx"])
        H = pickle.load(open("test_out.nx",'rb'))

        em = iso.numerical_edge_match('weight', 1)
        self.assertTrue(nx.is_isomorphic(self.G, H, edge_match=em))

    def test_cmdline_back_and_forth_with_header(self):
        for h in ("--header","--no-header"):
            pickle.dump(self.G, open("test_out.nx", 'wb'))

            su.check_call(["lntk-nx_to_csv", "test_out.nx", "test_nodes_csv", "test_edges_csv",h])

            su.check_call(["lntk-csv_to_nx", "test_nodes_csv", "test_edges_csv", "test_out.nx",h])
            H = pickle.load(open("test_out.nx", 'rb'))

            em = iso.numerical_edge_match('weight', 1)
            self.assertTrue(nx.is_isomorphic(self.G, H, edge_match=em))

class TestGif(unittest.TestCase):
    def setUp(self):
        from lntk.datasets.generated import get_gnp_series
        self.graphs = get_gnp_series(l=5)
        self.tmp_root = os.getcwd()+"/lntk/tests/tmp/"

    def tearDown(self):
        #Check if it has been created first?
        print(os.getcwd())
        teardown_remove_files([self.tmp_root+i for i in ["test.gif"]+["test_net"+str(i)+".nx" for i in range(5)]])

    def test_make_gif(self):
        net_files = []
        for i in range(5):
            filepath = self.tmp_root+"test_net"+str(i)+".nx"
            pickle.dump(self.graphs[i], open(filepath,"wb"))
            net_files.append(filepath)

        su.check_call(["lntk-nx_to_gif"] + net_files + ["test.gif"])

class TestRenderer(unittest.TestCase):
    def setUp(self):
        G = nx.gnp_random_graph(50,0.5)
        self.tmp_root = os.getcwd() + "/lntk/tests/tmp/"
        #        self.tmp_root = "src/tests/tmp/"

        #There is clearly optimisation potential here
        pickle.dump(G,open(self.tmp_root+"test.nx",'wb'))

    def tearDown(self):
        teardown_remove_files([self.tmp_root + i for i in ("test.nx", "test.html", "test.png","test.js")])

    def test_networkx_to_png(self):

        json.dump(defopt, open(self.tmp_root + "test.js", 'w'))
        su.check_call(["lntk-renderer"]+[self.tmp_root+x for x in ("test.nx","out.png")]+["png", self.tmp_root+"test.js"])
        Image.open(open(self.tmp_root + 'out.png', 'rb'))

    def test_layouts(self):
        all_layouts = list(ALL_CYTOSCAPE_PRESET_LAYOUTS)
        all_layouts.remove('preset')
        for layout in all_layouts:
            opt = deepcopy(defopt)
            opt['layout'] = layout
            json.dump(opt, open(self.tmp_root + "test.js", 'w'))

            su.check_call(["lntk-renderer"] + [self.tmp_root + x for x in ("test.nx", "out.png")] + ["png", self.tmp_root + "test.js"])
            Image.open(open(self.tmp_root + 'out.png', 'rb'))

    def test_valid_options(self):
        #  return
        options_to_test = {"node_size": ["betweeness", "closeness", "connectivity"], "shape": ["rectangle", ]}

        for key, values in options_to_test.items():
            for value in values:
                print("testing option " + str(key) + " with value " + str(value))
                opt = deepcopy(defopt)
                opt[key] = value
                json.dump(opt, open(self.tmp_root + "test.js", 'w'))
                su.check_call(["lntk-renderer"] + [self.tmp_root + x for x in ("test.nx", "out.png")] + ["png", self.tmp_root + "test.js"])
                Image.open(open(self.tmp_root + 'out.png', 'rb'))

