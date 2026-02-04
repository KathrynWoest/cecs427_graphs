import networkx as nx
import sys
import math

def generation(n, c):
    """Function that generates an Erdos Renyi graph given n nodes and c constant for probability that an edge exists between two nodes
    Inputs: strings n and c, representing the number of nodes and a constant to calculate probability of edges respectively
    Output: a NetworkX-structured Erdos-Renyi graph"""

    try:
        node_count = int(n)
        edge_const = int(c)

        # calculate probability of edges occuring with the given equation, then generate the graph
        edge_prob = edge_const * (math.log(node_count) / node_count)
        generated_graph = nx.erdos_renyi_graph(node_count, edge_prob)

    except ValueError as ve:
        print("Program terminated because graph generation input(s) 'n' and/or 'c' are not integers. Error message:", ve)
        sys.exit(1)

    except Exception as e:
        print("Program terminated because there was an error with NetworkX generating the graph or calculating p. Error message:", e)
        sys.exit(1)
    
    return generated_graph
