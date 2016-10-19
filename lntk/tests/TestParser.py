
import networkx.algorithms.isomorphism as iso
import os
import unittest
import networkx as nx
from lntk import parser


def teardown_remove_files(filepaths):
    if hasattr(filepaths,"__iter__"):
        for f in filepaths:
            if os.path.isfile(f):
                os.remove(f)
            else :
                raise AssertionError("A file was supposed to be generated at "+str(f)+" (not found).")

class CSV_parse_test(unittest.TestCase):
    def setUp(self):
        self.G = nx.generators.classic.complete_graph(10)

    def tearDown(self):
        teardown_remove_files(["test_node_csv","test_edges_csv"])

    def test_back_and_forth(self):
        ncsv, ecsv = "test_node_csv","test_edges_csv"

        parser.networkx_to_csv(self.G, ncsv, ecsv)
        H = parser.csv_to_networkx(ncsv, ecsv)

        print(self.G.nodes())
        print(H.nodes())
        print(self.G.edges(), H.edges())

        #Test isomorphism
        em = iso.numerical_edge_match('weight', 1)
        self.assertTrue(nx.is_isomorphic(self.G, H, edge_match=em))

        #Test id and attributes - invalid test see note below
    #    self.assertTrue(self.G.nodes() == H.nodes())
    #    self.assertTrue(self.G.edges() == H.eges())

        # N.B. everything imported as csv is considered a string
        #TODO : test attributes
