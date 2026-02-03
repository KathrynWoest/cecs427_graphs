import networkx as nx
import sys

def main():

    # if allowed to, can use nx.erdos_renyi_graph(n, c) to generate the graph
    # if not allowed to:
    #   create a generation file and loop through n nodes, manually writing each line to the file for the nodes
    #   then use a for loop to iterate through every possible edge in the graph
    #   the loop will randomly generate a number and compare it to c to determine if the edge exists
    #   if it does, manually write the edge lines into the file
    #   then read the file in with nx.parse_gml(file) to set it up as a networkx graph for analysis
    #   finally, delete the generation file (if that's possible?), as it won't be needed again


    pass

main()