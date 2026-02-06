import networkx as nx

def analyze(graph):
    """
    Analyze the structural properties of a NetworkX graph and compute
    data for visualization.

    Args:
        graph (networkx.Graph) : the input graph to analyze

    Returns:
        dict: 
            A dictionary containing:
            - 'graph' (networkx.Graph) : the original graph
            - 'components' (list of sets) : each set contains the nodes in one connected component
            - 'isolated_nodes' (list) : a list of nodes with no incident edges
            - 'highlight_edges' (set of tuples) : a set of edges (u, v) that appear in at least 
                one shortest path computed via breadth-first search / Dijkstra
    """
    
    # Loading the graph
    G = nx.read_gml(graph)

    # Looking for connected components
    components = list(nx.connected_components(G))
    num_components = len(components)
    print("Connected components:", num_components)

    # Detecting cycles
    has_cycle = 0
    if (nx.is_directed(G)):
        has_cycle = not nx.is_directed_acyclic_graph(G)
    else:
        has_cycle = len(nx.cycle_basis(G)) > 0

    result = 0
    if has_cycle:
        result = "Yes"
    else:
        result = "No"

    print("Contains cycle?:", result)

    # Detecting isolated nodes
    isolated_nodes = list(nx.isolates(G))
    print("Isolated nodes:", isolated_nodes)

    # Computing density
    density = nx.density(G)
    print("Graph density:", density)

    # # Computing BFS shortest paths
    # bfs_roots = [next(iter(c)) for c in components]

    # lengths, paths = nx.multi_source_dijkstra(graph, bfs_roots)

    # # Marking edges that belong to any shortest path
    # highlight_edges = set()
    # for target, path in paths.items():
    #     if len(path) > 1:
    #         edges = zip(path[:-1], path[1:])
    #         highlight_edges.update(edges)

    # Computing average shortest path length
    if nx.is_connected(G):
        avg_path_len = nx.average_shortest_path_length(G)
        print("Average shortest path length:", avg_path_len)
    else:
        print("Graph is not connected; cannot compute average shortest path length.")

    return {
        "graph": G,
        "components": components,            # list of sets
        "isolated_nodes": isolated_nodes,    # list
    }


def multi_bfs(graph, start_nodes):
    """
    Perform independent BFS traversals from multiple starting nodes.

    Each starting node generates its own BFS tree and set of shortest paths.
    Traversals are independent and do not compete with one another.

    Parameters:
    graph (networkx.Graph) : the graph on which BFS will be performed.
    start_nodes (list) : a list of starting nodes for BFS.

    Returns:
        dict:
            A dictionary mapping each starting node to its BFS result:
            {
                start_node: {
                    target_node: [path from start_node to target_node]
                }
            }

    Raises:
        ValueError
            If a starting node is not present in the graph.
    """

    bfs_results = {}

    for src in start_nodes:
        if src not in graph:
            raise ValueError(f"BFS start node {src} is not in the graph.")
        
        paths = nx.single_source_shortest_path(graph, src)

        bfs_results[src] = paths

    return bfs_results