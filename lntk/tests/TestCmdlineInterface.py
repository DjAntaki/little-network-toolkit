import networkx.algorithms.isomorphism as iso
import os
import pickle
import subprocess as su
import unittest
import networkx as nx
from lntk import visual_utils

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

#        visual_utils.graph_sequence_to_gif("lntk/tests/tmp/test.gif", self.graphs, tmp_location=self.tmp_root)
