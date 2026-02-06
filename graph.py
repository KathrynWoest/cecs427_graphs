import sys
import generator as gen
import file_io as fio

def main():
    # get arguments from command line and initialize BFS node list, the iterator to traverse arguments, and the end of the argument list
    args = sys.argv
    multi_BFS_nodes = []
    iterator = 1
    end = len(args)

    # if there are less than 3 arguments, then not possible to do anything. terminate program.
    if end < 3:
        raise Exception(f"Program was terminated because there are not enough arguments to upload or generate a graph. Minimum required arguments: 2. Arguments provided: {end}.")
    
    else:
        # parse in graph from given .gml file
        if args[1] == "--input":
            input_file = args[2]
            user_graph = fio.parse_graph(input_file)
            iterator += 2
        # generate graph with given n and c, override --input graph with --create graph
        if end > 3 and args[1] == "--create_random_graph":
            n = args[2]
            c = args[3]
            user_graph = gen.generation(n, c)
            iterator += 3
        # if there are 3 arguments and we aren't inputting a file, then not enough arguments to generate graph. terminate program.
        else:
            raise Exception("Program was terminated because it was missing '--create_random_graph arguments'. Requires 'n' (number of nodes) and 'c' (probability of an edge forming).")

        # make a list of all BFS nodes given and call the BFS function
        if iterator < end and args[iterator] == "--multi_BFS":
            remaining_args = args[iterator + 1:]

            for i in range(len(remaining_args)):
                # check if the current argument is the next command and not another node. if it's the next command, stop iterating.
                if "--" not in remaining_args[i]:
                    multi_BFS_nodes.append(remaining_args[i])
                else:
                    iterator += i + 1
                    break
            
            if len(multi_BFS_nodes) == 0:
                raise Exception("Program was terminated because it was missing starting node(s) for the BFS analysis.")
            
            # TODO: call BFS from analysis: result = BFS(user_graph, multi_BFS_nodes)
        
        # call the analysis function
        if iterator < end and args[iterator] == "--analyze":
            # TODO: call analysis from analysis: result = analysis(user_graph)
            iterator += 1
        
        # call the visualization function
        if iterator < end and args[iterator] == "--plot":
            # TODO: call plot from visualization: result = visualization(user_graph)
            iterator += 1
        
        # call the output function
        if iterator < end and args[iterator] == "--output":
            # check if the output file name is missing. if so, terminate program.
            if iterator + 1 == end:
                raise Exception("Program was terminated because it was missing the output file name.")
            
            output_file = args[iterator + 1]
            iterator += 2
            fio.save_graph(user_graph, output_file)
        
        # check to see if there are extra arguments provided. if so, print them so the user can see.
        if iterator < end:
            print("NOTE: extra arguments at the end of the input string were ignored:", args[iterator:])

main()
