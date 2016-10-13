
import unittest
import networkx as nx
#from src.scripts import visual_utils as vu
from src.scripts import load_network as ln

class CSV_parse_test(unittest.TestCase):
    def setUp(self):
        self.G = nx.generators.classic.complete_graph(10)


            #nx.generators.cluster_sequence()
        pass

    def test_back_and_forth(self):
        ncsv, ecsv = "test_node_csv","test_edges_csv"

        ln.networkx_to_csv(self.G,ncsv,ecsv)
        H = ln.csv_to_networkx(ncsv,ecsv)
