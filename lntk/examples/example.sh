export PATH=$PATH:/path_to_nodejs/node_modules/geckodriver
lntk-nx_to_csv complete_graph.nx example_nodes.csv example_edges.csv
lntk-csv_to_nx example_nodes.csv example_edges.csv complete_graph.nx
lntk-renderer complete_graph.nx complete_graph.png png example.js 
lntk-renderer complete_graph.nx complete_graph.html html example.js
lntk-nx_to_gif complete_graph.nx complete_graph.gif
