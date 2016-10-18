import unittest
import networkx as nx
from src.scripts import manipulations as nm

class TestManipulationUndirectedGraph(unittest.TestCase):
    def setUp(self):
        self.G = nx.complete_bipartite_graph(5,10)


    def test_merge_invalid_node_id(self):
       # self.assertRaises()
        pass

    def test_merge_nodes(self):
        to_merge_node_id = (1,2,3)

        print(self.G.nodes())

        #Retrieve associated edges.
        edges_to_be_merged = []
        edges_not_to_be_merged = []
        for i,j in self.G.edges():
            if i in to_merge_node_id or j in to_merge_node_id:
                edges_to_be_merged.append((i,j))
            else :
                edges_not_to_be_merged.append((i,j))

        nm.merge_nodes(self.G, to_merge_node_id, "newnode")

        i = 0
        for i,j in edges_not_to_be_merged:
            self.G[i][j]
            i += 1

        for i,j in edges_to_be_merged:
            if i in to_merge_node_id:
                if j in to_merge_node_id:
                    self.G["newnode"]["newnode"]
                else :
                    self.G["newnode"][j]
            elif j in to_merge_node_id:
                self.G[i]["newnode"]
            else :
                raise Exception('Something very wrong happen')
            i += 1

        assert all([not n in self.G.nodes() for n in to_merge_node_id])

    def test_update_nodes_data(self):
        new_data = {n:34 for n in self.G.nodes()}
        nm.update_network_node_data(self.G,"new_id",new_data)
        nodes_attr = nx.get_node_attributes(self.G, "new_id")
        for n in self.G.nodes():
            print(nodes_attr)
            self.assertTrue( nodes_attr[n]== 34)

    def test_update_edges_data(self):
        new_data = {(i,j):34 for i,j in self.G.edges()}
        print(self.G.edges())
        nm.update_network_edge_data(self.G,"new_id",new_data)
        print(self.G.edges())
        print(new_data)
        for i,j in self.G.edges():
            self.assertTrue(self.G[i][j]["new_id"] == 34)

if __name__ == '__main__':
    unittest.main()
