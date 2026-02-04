import networkx as nx
import iplotx as ipx

def plot(graph, components, isolated_nodes, highlight_edges):
    # Node styling and attributes
    for n in graph.nodes():
        graph.nodes[n]["degree"] = graph.degree(n)
        graph.nodes[n]["component"] = next(i for i, comp in enumerate(components) if n in comp)

        if n in isolated_nodes:
            graph.nodes[n]["color"] = "red"
            graph.nodes[n]["size"] = 20
            graph.nodes[n]["label"] = f"{n} (isolated)"
        else:
            graph.nodes[n]["color"] = "skyblue"
            graph.nodes[n]["size"] = 12
            graph.nodes[n]["label"] = str(n)

    # Edge styling
    for u, v in graph.edges():
        if (u, v) in highlight_edges or (v, u) in highlight_edges:
            graph.edges[u, v]["color"] = "orange"
            graph.edges[u, v]["width"] = 3
        else:
            graph.edges[u, v]["color"] = "lightgray"
            graph.edges[u, v]["width"] = 1

    # Legend nodes
    legend_items = {
        "Isolated Node": {"color": "red", "size": 20},
        "Normal Node": {"color": "skyblue", "size": 12},
        "Shortest Path Edge": {"color": "orange", "size": 12},
    }

    for label, attrs in legend_items.items():
        legend_node = f"legend_{label}"
        graph.add_node(legend_node, **attrs, label=label, legend=True)

    # Defining layout
    pos = nx.spring_layout(graph)
    offset = 2.0

    for i, label in enumerate(legend_items):
        legend_node = f"legend_{label}"
        pos[legend_node] = (offset, -i * 0.3)

    # Plotting graph
    ipx.plot(graph, title="Graph with BFS Shortest Paths & Isolated Node Styling")
