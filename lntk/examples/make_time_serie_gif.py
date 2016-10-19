from lntk.visual_utils import graph_sequence_to_gif
from lntk.datasets.generated import get_gnp_series

graphs = get_gnp_series()

graph_sequence_to_gif("test.gif",graphs)

