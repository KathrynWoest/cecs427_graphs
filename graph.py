import sys
import generator as gen
import file_io as fio
import plot
import analyze

def main():
    # get arguments from command line and initialize BFS node list, the end of the argument list, and bools for which analyses were called
    args = sys.argv
    multi_BFS_nodes = []
    end = len(args)
    called_BFS = False
    called_analysis = False

    # if there are less than 3 arguments, then not possible to do anything. terminate program.
    if end < 3:
        raise Exception(f"Program was terminated because there are not enough arguments to upload or generate a graph. Minimum required arguments: 2. Arguments provided: {end}.")
    
    # parse or generate graph
    else:
        # parse in graph from given .gml file
        if "--input" in args and "--create_random_graph" not in args:
            input_file = args[args.index("--input") + 1]
            user_graph = fio.parse_graph(input_file)
        # generate graph with given n and c, override --input graph with --create graph
        elif end > 3 and "--create_random_graph" in args:
            n = args[args.index("--create_random_graph") + 1]
            c = args[args.index("--create_random_graph") + 2]
            user_graph = gen.generation(n, c)
        # if there are 3 arguments and we aren't inputting a file, then not enough arguments to generate graph. terminate program.
        else:
            raise Exception("Program was terminated because it was missing '--create_random_graph arguments'. Requires 'n' (number of nodes) and 'c' (probability of an edge forming).")

        # make a list of all BFS nodes given and call the BFS function
        if "--multi_BFS" in args:
            called_BFS = True
            remaining_args = args[args.index("--multi_BFS") + 1:]

            for i in range(len(remaining_args)):
                # check if the current argument is the next command and not another node. if it's the next command, stop iterating.
                if "--" not in remaining_args[i]:
                    multi_BFS_nodes.append(int(remaining_args[i]))
                else:
                    break
            
            if len(multi_BFS_nodes) == 0:
                raise Exception("Program was terminated because it was missing starting node(s) for the BFS analysis.")
            
            shortest_paths = analyze.multi_bfs(user_graph, multi_BFS_nodes)
        
        # call the analysis function
        if "--analyze" in args:
            called_analysis = True
            analysis = analyze.analyze(user_graph, called_analysis)
        
        # call the visualization function
        if "--plot" in args:
            # set up the resulting BFS shortest_paths to be a set of edges for the plotting
            if called_BFS:
                bfs_edges = {}
                edges = set()

                # narrows it down to just srcs and their edges
                for src, data in shortest_paths.items():
                    bfs_edges[src] = data["edges"]

                # flattens it down to just being a set of the edges
                for edge_set in bfs_edges.values():
                    edges.update(edge_set)

            # check to see which version of the plot to call based on what analysis/BFS was completed
            if called_BFS and called_analysis:
                plot.plot(user_graph, analysis["isolated_nodes"], edges, called_BFS)
            elif not called_BFS and called_analysis:
                plot.plot(user_graph, analysis["isolated_nodes"])
            elif called_BFS and not called_analysis:
                analysis = analyze.analyze(user_graph)
                plot.plot(user_graph, analysis["isolated_nodes"], edges, called_BFS)
        
        # call the output function
        if "--output" in args:
            # check if the output file name is missing. if so, terminate program.
            if args.index("--output") + 1 == end:
                raise Exception("Program was terminated because it was missing the output file name.")
            
            output_file = args[args.index("--output") + 1]

            # check to see if any/which analysis needs to be saved with the graph
            if called_BFS and called_analysis:
                fio.save_graph(user_graph, output_file, shortest_paths, analysis)
            elif not called_BFS and called_analysis:
                fio.save_graph(user_graph, output_file, {}, analysis)
            elif called_BFS and not called_analysis:
                fio.save_graph(user_graph, output_file, shortest_paths)
            else:
                fio.save_graph(user_graph, output_file)

main()
