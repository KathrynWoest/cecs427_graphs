import networkx as nx
import iplotx as ipx

def plot(graph, isolated_nodes, highlight_edges):
    for n in graph.nodes():
        if n in isolated_nodes:
            graph.nodes[n]["color"] = "red"
            graph.nodes[n]["size"] = 20
        else:
            graph.nodes[n]["color"] = "skyblue"
            graph.nodes[n]["size"] = 12

    for u, v in graph.edges():
        if (u, v) in highlight_edges or (v, u) in highlight_edges:
            graph.edges[u, v]["color"] = "orange"
            graph.edges[u, v]["width"] = 3
        else:
            graph.edges[u, v]["color"] = "lightgray"
            graph.edges[u, v]["width"] = 1

    ipx.plot(graph, title="Graph with BFS Shortest Paths & Isolated Node Styling")
