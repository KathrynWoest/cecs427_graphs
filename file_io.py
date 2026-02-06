import sys
import networkx as nx

def parse_graph(file_name):
    """Takes the input file and parses it into a NetworkX graph that can be analyzed
    Input: .gml file name of the submitted graph
    Output: NetworkX graph of the submitted graph from the file"""
    
    if ".gml" not in file_name:
        raise Exception("Input file type is not .gml. Provided file:", file_name)

    try:
        # reads .gml file and parses it into the graph
        submitted_graph = nx.read_gml(file_name)
        return submitted_graph
    
    except Exception as e:
        print("Program quit due to an error in reading and parsing the graph from the provided .gml file.")
        print("Provided error:", e)
        sys.exit(1)

def save_graph(graph, file_name, bfs_paths={}, analysis={}):
    """Takes a name for an output file, creates the file, and saves the graph and any analysis into it
    Inputs: the graph itself, .gml file name for saving the graph
    Output: none"""

    if ".gml" not in file_name:
        raise Exception("Output file type is not .gml. Provided file:", file_name)
    
    try:
        # save all analysis to the graph structure before saving the graph to the output file
        if len(bfs_paths) > 0:
            # if there are BFS paths to save, save them
            for node_id, path in bfs_paths.items():
                graph.nodes[node_id]["Calculated BFS paths"] = path
        if len(analysis) > 0:
            # if there's analysis to save, save it

            # add component information to nodes
            components = analysis["components"]
            component_id = 0
            for component in components:
                for node in component:
                    node["Component ID"] = component_id
                    node["Other nodes in component"] = [x for x in component if x != node]
                    node["Node is isolated"] = False
                component_id += 1

            # add isolated node information
            isolated = analysis["isolated_nodes"]
            for node in isolated:
                node["Node is isolated"] = True

    except Exception as e:
        print("Program quit due to an error in saving analysis to the graph.")
        print("Provided error:", e)
        sys.exit(1)

    try:
        # creates output file and writes graph to it
        nx.write_gml(graph, file_name)

    except Exception as e:
        print("Program quit due to an error in creating the save file and saving the graph.")
        print("Provided error:", e)
        sys.exit(1)
