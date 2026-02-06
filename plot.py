import networkx as nx
from pyvis.network import Network
import os
import webbrowser

def plot(graph, isolated_nodes, highlight_edges=(), bfs_called=False):
    """
    Visualize a NetworkX graph using PyVis with customized styling and
    an interactive legend.

    Args:
        graph (networkx.Graph) : the graph to visualize
        isolated_nodes (list) : a list of nodes that are isolated (degree zero) in the graph
        highlight_edges (set of tuples) : a set of edges (u, v) that should be visually emphasized,
            representing shortest-path edges.

    Notes:
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
                edge["color"] = "#d0d0d0"
                edge["width"] = 2
        else:
            edge["color"] = "#d0d0d0"
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

    # Generate HTML
    net.write_html("graph.html", open_browser=False)

    # Post-process HTML to add title
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

    webbrowser.open("graph.html")
