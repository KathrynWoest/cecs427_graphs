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
    isolated = list(nx.isolates(G))
    print("Isolated nodes:", isolated)

    # Computing density
    density = nx.density(G)
    print("Graph density:", density)

    # Average shortest path length
    if nx.is_connected(G):
        avg_path_len = nx.average_shortest_path_length(G)
        print("Average shortest path length:", avg_path_len)
    else:
        print("Graph is not connected; cannot compute average shortest path length.")