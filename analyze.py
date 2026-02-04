import networkx as nx

def analyze(graph):
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

    # Computing average shortest path length
    if nx.is_connected(G):
        avg_path_len = nx.average_shortest_path_length(G)
        print("Average shortest path length:", avg_path_len)
    else:
        print("Graph is not connected; cannot compute average shortest path length.")

    ## Data for plotting ##
    # Computing BFS shortest paths from each root
    bfs_roots = [next(iter(c)) for c in components]

    shortest_paths = []
    for root in bfs_roots:
        lengths, paths = nx.single_source_dijkstra(G, root)  # works for weighted or unweighted
        shortest_paths.append(paths)

    # Marking edges that belong to any shortest path
    highlight_edges = set()
    for paths in shortest_paths:
        for target, path in paths.items():
            if len(path) > 1:
                edges = list(zip(path[:-1], path[1:]))
                highlight_edges.update(edges)


    return G, isolated_nodes, highlight_edges, components