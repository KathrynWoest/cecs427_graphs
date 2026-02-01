import sys
import networkx as nx

# will temporarily use this as the main file for testing purposes

def parse_graph(file_name):
    """Takes the input file and parses it into a NetworkX graph that can be analyzed
    Input: file name of the submitted graph
    Output: NetworkX graph of the submitted graph from the file"""

    # okay only keep this if there's error handling i can add, bc otherwise kind of a useless function lol
    submitted_graph = nx.read_gml(file_name)
    return submitted_graph

def main():
    args = sys.argv
    file_path = args[1]
    og_graph = parse_graph(file_path)

main()
