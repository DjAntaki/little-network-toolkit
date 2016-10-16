import unittest
import networkx as nx
from src.scripts import network_manipulations as nm

class TestManipulationUndirectedGraph(unittest.TestCase):
    def setUp(self):
        self.G = nx.Graph()

        self.H = nx.Graph()

    def test_merge_invalid_node_id(self):
        pass

    def test_merge_nodes(self):
        to_merge_node_id = (1,2,3)

        #Retrieve associated edges.
        edges = []
        for i,j in self.G.edges():
            pass
        nm.merge_nodes(self.G, to_merge_node_id, "newnode")

        for i,j in self.G.edges():
            pass

    def test_update_nodes_data(self):
        new_data = {n:34 for n in self.G.nodes()}
        nm.update_network_node_data(self.G,"new_id",new_data)
        for n in self.G.nodes():
            self.assertTrue(self.G[n]["new_id"] == 34)

    def test_update_edges_data(self):
        new_data = {(i,j):34 for i,j in self.G.edges()}
        nm.update_network_node_data(self.G,"new_id",new_data)
        for n in self.G.edges():
            self.assertTrue(self.G[i][j]["new_id"] == 34)

if __name__ == '__main__':
    unittest.main()
