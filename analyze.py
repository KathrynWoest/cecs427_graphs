import networkx as nx
from pyvis.network import Network
import os
import webbrowser

def analyze(graph, analyze_called=False):
    """
    Analyze the structural properties of a NetworkX graph and compute
    data for visualization.

    Args:
        graph (networkx.Graph) : the input graph to analyze
        analyze_called (bool) : flag for stopping graph analysis reults from printing
            when --plot is called before --analyze

    Returns:
        dict: 
            A dictionary containing:
            - 'graph' (networkx.Graph) : the original graph
            - 'components' (list of sets) : each set contains the nodes in one connected component
            - 'isolated_nodes' (list) : a list of nodes with no incident edges
    """
    
    # Loading the graph
    G = graph

    # Looking for connected components
    components = list(nx.connected_components(G))
    num_components = len(components)
    if analyze_called:
        print("Connected components:", num_components)

    # Detecting cycles
    has_cycle = 0
    if (nx.is_directed(G)):
        has_cycle = not nx.is_directed_acyclic_graph(G)
    else:
        has_cycle = len(nx.cycle_basis(G)) > 0

    if analyze_called:
        result = 0
        if has_cycle:
            result = "Yes"
        else:
            result = "No"

        print("Contains cycle?:", result)

    # Detecting isolated nodes
    isolated_nodes = list(nx.isolates(G))
    if analyze_called:
        print("Isolated nodes:", isolated_nodes)

    # Computing density
    density = nx.density(G)
    if analyze_called:
        print("Graph density:", density)

    # Computing average shortest path length
    if nx.is_connected(G):
        avg_path_len = nx.average_shortest_path_length(G)
        if analyze_called:
            print("Average shortest path length:", avg_path_len)
    else:
        if analyze_called:
            print("Graph is not connected; cannot compute average shortest path length.")

    return {
        "graph": G,
        "components": components,            # list of sets
        "isolated_nodes": isolated_nodes,    # list
    }


def multi_bfs(graph, start_nodes):
    """
    Perform independent BFS traversals from multiple starting nodes and plots each BFS tree.

    For each source node, this function:
    - Computes the BFS tree
    - Stores shortest-path distances (edge count)
    - Optionally visualizes the BFS tree using a hierarchical layout

    Args:
        graph (networkx.Graph) : the graph on which BFS will be performed.
        start_nodes (list) : a list of starting nodes for BFS.

    Returns:
        dict:
            A mapping of the form:
            {
                source_node: {
                    "edges": set[(u, v)],
                    "distances": dict[node -> int]
                }
            }

    Raises:
        ValueError
            If a starting node is not present in the graph.
    """

    bfs_results = {}

    for src in start_nodes:
        src = str(src)
        if src not in graph:
            raise ValueError(f"BFS start node {src} is not in the graph.")
        
        tree_edges = list(nx.bfs_edges(graph, src))
        distances = dict(nx.single_source_shortest_path_length(graph, src))

        highlight_edges = set()

        # Shortest paths from this source
        paths = nx.single_source_shortest_path(graph, src)

        # Extract edges from each shortest path
        for path in paths.values():
            if len(path) > 1:
                highlight_edges.update(zip(path[:-1], path[1:]))

        bfs_results[src] = {
            "edges": highlight_edges,
            "distances": distances
        }

        ## Plotting BFS Graphs ##
        # Build BFS tree graph
        T = nx.Graph()
        T.add_edges_from(tree_edges)

        # Ensure root exists even if isolated
        T.add_node(src)

        net = Network(
            height="750px",
            width="100%",
            directed=True,
            bgcolor="#ffffff"
        )

        net.from_nx(T)

        # Force hierarchical tree layout
        net.set_options("""
        {
            "layout": {
            "hierarchical": {
                "enabled": true,
                "direction": "UD",
                "sortMethod": "directed"
            }
            },
            "physics": {
            "hierarchicalRepulsion": {
                "nodeDistance": 120
            }
            }
        }
        """)

        # Node styling
        for node in net.nodes:
            if int(node["id"]) == src:
                node["color"] = "#2a9d8f"
                node["size"] = 28
                node["label"] = f"{node['id']}"
            else:
                node["color"] = "#9ecae1"
                node["size"] = 16
                node["label"] = f"{node['id']}"

        # Legend
        legend_x = -350
        legend_y = -100
        spacing = 60

        net.add_node(
            "legend_title",
            label="LEGEND",
            x=legend_x,
            y=legend_y,
            fixed=True,
            physics=False,
            shape="box",
            color="#f0f0f0",
            font={"size": 16, "bold": True}
        )

        legend_items = [
            ("legend_root", "BFS Root", "#2a9d8f", 26),
            ("legend_node", "BFS Tree Node", "#9ecae1", 16),
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

        # Generate HTML
        net.write_html(f"bfs_tree_{src}.html", open_browser=False)

        # Post-process HTML to add title
        title_html = f"""
        <h2 id="graph-title" style="
            text-align:center;
            font-family:Arial, sans-serif;
            color:#222;
            margin: 10px 0 20px 0;
        ">
        BFS Tree (from {src})
        </h2>
        """

        if os.path.exists(f"bfs_tree_{src}.html"):
            with open(f"bfs_tree_{src}.html", "r", encoding="utf-8") as f:
                html = f.read()

            if 'id="graph-title"' not in html:
                html = html.replace("<body>", "<body>\n" + title_html, 1)

                with open(f"bfs_tree_{src}.html", "w", encoding="utf-8") as f:
                    f.write(html)

        webbrowser.open(f'bfs_tree_{src}.html')

    return bfs_results