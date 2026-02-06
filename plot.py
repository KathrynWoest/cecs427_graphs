import networkx as nx
from pyvis.network import Network
import os

def plot(graph, isolated_nodes, highlight_edges, bfs_called=True):
    """
    Visualize a NetworkX graph using PyVis with customized styling and
    an interactive legend.

    Args:
    graph (networkx.Graph) : the graph to visualize
    isolated_nodes (list) : a list of nodes that are isolated (degree zero) in the graph
    highlight_edges (set of tuples) : a set of edges (u, v) that should be visually emphasized,
        representing shortest-path edges.

    Notes
    -----
    - This function generates an interactive HTML file using PyVis.
    - Visualization styling does not modify the underlying graph structure.
    - The resulting visualization is saved as 'graph.html'.
    """

    net = Network(
        height="750px",
        width="100%",
        bgcolor="#ffffff",
        font_color="#222222"
    )

    # Loading NetworkX graph
    net.from_nx(graph)

    # Styling nodes
    for node in net.nodes:
        n = int(node["id"])

        if n in isolated_nodes:
            node["label"] = f"{n} (isolated)"
            node["size"] = 22
            node["color"] = {
                "background": "#ff6b6b",
                "border": "#b22222"
            }
        else:
            node["label"] = str(n)
            node["size"] = 16
            node["color"] = {
                "background": "#9ecae1",
                "border": "#4682b4"
            }

    # Styling edges
    for edge in net.edges:
        u, v = int(edge["from"]), int(edge["to"])
        highlighted = (u, v) in highlight_edges or (v, u) in highlight_edges

        if bfs_called:
            if highlighted:
                edge["color"] = "#f4a261"
                edge["width"] = 3
            else:
                edge["color"] = "#d0d0d000"
                edge["width"] = 2
        else:
            edge["color"] = "#d0d0d000"
            edge["width"] = 2
            
        edge["smooth"] = {"type": "continuous"}

    # Styled legend panel
    legend_x = -380
    legend_y = -120
    spacing = 60

    # Legend title
    net.add_node(
        "legend_title",
        label="LEGEND",
        x=legend_x,
        y=legend_y,
        fixed=True,
        physics=False,
        shape="box",
        color="#f7f7f7",
        font={"size": 16, "bold": True}
    )

    legend_items = [
        ("legend_iso", "Isolated Node", "#ff6b6b", 18),
        ("legend_norm", "Normal Node", "#9ecae1", 14),
        ("legend_edge", "BFS Shortest Path \n(from root)", "#f4a261", 14),
    ]

    for i, (nid, label, color, size) in enumerate(legend_items, start=1):
        net.add_node(
            nid,
            label=label,
            color=color,
            size=size,
            x=legend_x,
            y=legend_y + i * spacing,
            fixed=True,
            physics=False,
            selectable=False
        )

    net.toggle_physics(False)

    # Generate HTML FIRST
    net.write_html("graph.html", open_browser=False)

    # ---- Post-process HTML to add title (safe) ----
    title_html = """
    <h2 id="graph-title" style="
        text-align:center;
        font-family:Arial, sans-serif;
        color:#222;
        margin: 10px 0 20px 0;
    ">
    Graph Visualization Highlighting Connected Components,
    Shortest Paths, and Isolated Nodes
    </h2>
    """

    if os.path.exists("graph.html"):
        with open("graph.html", "r", encoding="utf-8") as f:
            html = f.read()

        if 'id="graph-title"' not in html:
            html = html.replace("<body>", "<body>\n" + title_html, 1)

            with open("graph.html", "w", encoding="utf-8") as f:
                f.write(html)


# ###### Testing #######
# def make_test_graph():
#     G = nx.Graph()

#     # Component 1: A triangle (cycle)
#     G.add_edges_from([(1, 2), (2, 3), (3, 1)])

#     # Component 2: A simple chain
#     G.add_edges_from([(4, 5), (5, 6)])

#     # Isolated node
#     G.add_node(7)

#     return G

# def analyze(graph):
#     """
#     Analyze the structural properties of a NetworkX graph and compute
#     data for visualization.

#     Args:
#         graph (networkx.Graph) : the input graph to analyze

#     Returns:
#         dict: 
#             A dictionary containing:
#             - 'graph' (networkx.Graph) : the original graph
#             - 'components' (list of sets) : each set contains the nodes in one connected component
#             - 'isolated_nodes' (list) : a list of nodes with no incident edges
#             - 'highlight_edges' (set of tuples) : a set of edges (u, v) that appear in at least 
#                 one shortest path computed via breadth-first search / Dijkstra
#     """

#     # Loading the graph
#     #G = nx.read_gml(graph)
#     G = graph # test graph

#     # Looking for connected components
#     components = list(nx.connected_components(G))
#     num_components = len(components)
#     print("Connected components:", num_components)

#     # Detecting cycles
#     has_cycle = 0
#     if (nx.is_directed(G)):
#         has_cycle = not nx.is_directed_acyclic_graph(G)
#     else:
#         has_cycle = len(nx.cycle_basis(G)) > 0

#     result = 0
#     if has_cycle:
#         result = "Yes"
#     else:
#         result = "No"

#     print("Contains cycle?:", result)

#     # Detecting isolated nodes
#     isolated_nodes = list(nx.isolates(G))
#     print("Isolated nodes:", isolated_nodes)

#     # Computing density
#     density = nx.density(G)
#     print("Graph density:", density)

#     # Computing average shortest path length
#     if nx.is_connected(G):
#         avg_path_len = nx.average_shortest_path_length(G)
#         print("Average shortest path length:", avg_path_len)
#     else:
#         print("Graph is not connected; cannot compute average shortest path length.")

#     ## Data for plotting ##
#     # Computing BFS shortest paths
#     bfs_roots = [next(iter(c)) for c in components]

#     lengths, paths = nx.multi_source_dijkstra(graph, bfs_roots)

#     # Marking edges that belong to any shortest path
#     highlight_edges = set()
#     for target, path in paths.items():
#         if len(path) > 1:
#             edges = zip(path[:-1], path[1:])
#             highlight_edges.update(edges)

#     return {
#         "graph": G,
#         "components": components,            # list of sets
#         "isolated_nodes": isolated_nodes,    # list
#         "highlight_edges": highlight_edges,  # set of tuples
#     }


# test_graph = make_test_graph()
# results = analyze(test_graph)   # data needed for visualization

# # Adding title to graph metadata
# results["graph"].graph["title"] = (
#     "Graph Visualization Highlighting Connected Components, "
#     "Shortest Paths, and Isolated Nodes"
# )

# nx.write_gml(results["graph"], "graph.gml")     # to export to .gml

# plot(
#     results["graph"],
#     results["isolated_nodes"],
#     results["highlight_edges"]
# )
