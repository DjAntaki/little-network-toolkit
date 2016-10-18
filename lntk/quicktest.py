import lntk.scripts.nx_to_gif
from datasets import generated
from scripts import visual_utils as vu
from selenium import webdriver

def new_driver():
    return webdriver.Firefox()

gnp = generated.get_gnp_series()
#html0 = vu.networkx_to_cytoscape_html(gnp[0],"test.html")
#browser = new_driver()

#print(__file__)
#returned = vu.html_to_png("test.html",save=True)
#print(returned)

lntk.scripts.nx_to_gif.graph_sequence_to_gif("test.gif", gnp)