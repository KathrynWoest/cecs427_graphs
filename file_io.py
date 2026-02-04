import sys
import networkx as nx

def parse_graph(file_name):
    """Takes the input file and parses it into a NetworkX graph that can be analyzed
    Input: .gml file name of the submitted graph
    Output: NetworkX graph of the submitted graph from the file"""
    
    try:
        # reads .gml file and parses it into the graph
        submitted_graph = nx.read_gml(file_name)
        return submitted_graph
    
    except Exception as e:
        print("Program quit due to an error in reading and parsing the graph from the provided .gml file.")
        print("Provided error:", e)
        sys.exit(1)

def save_graph(graph, file_name):
    """Takes a name for an output file, creates the file, and saves the graph and any analysis into it
    Inputs: the graph itself, .gml file name for saving the graph
    Output: none"""

    try:
        # creates output file and writes graph to it
        nx.write_gml(graph, file_name)

    except Exception as e:
        print("Program quit due to an error in creating the save file and saving the graph.")
        print("Provided error:", e)
        sys.exit(1)
