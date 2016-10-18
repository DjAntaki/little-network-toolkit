from src.scripts.nx_to_gif import graph_sequence_to_gif
from src.datasets.generated import get_gnp_series

graphs = get_gnp_series()

graph_sequence_to_gif("test.gif",graphs)

