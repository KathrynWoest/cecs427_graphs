import networkx as nx
import iplotx as ipx

def plot(graph):
    ipx.network(
        graph, 
        layout="tree",
        vertex_marker="s",
        vertex_size=45,
        vertex_linewidth=2,
        # vertex_facecolor=[
        #     "lightblue" if gender == "M" else "deeppink" for gender in g.vs["gender"]
        # ],
        # vertex_label_color=[
        #     "black" if gender == "M" else "white" for gender in g.vs["gender"]
        # ],
        # vertex_edgecolor="black",
        # vertex_labels=[name.replace(" ", "\n") for name in g.vs["name"]],
        # edge_linewidth=[2 if married else 1 for married in g.es["married"]],
        # edge_color=["#7142cf" if married else "#AAA" for married in g.es["married"]],
        # edge_padding=3,
        # aspect=1.0,
    )
