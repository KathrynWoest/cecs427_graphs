import sys

def main():
    args = sys.argv
    multi_BFS_nodes = []
    iterator = 1
    end = len(args)

    if end < 3:
        raise Exception(f"Program was terminated because there are not enough arguments to upload or generate a graph. Minimum required arguments: 2. Arguments provided: {end}.")
    
    else:
        if args[1] == "--input":
            input_file = args[2]
            # TODO: call file parser from file_io: user_graph = fio.parse_graph(input_file)
            iterator += 2
        elif end > 3 and args[1] == "--create_random_graph":
            n = args[2]
            c = args[3]
            # TODO: call graph generator from generator: user_graph = gen.generate(n, c) <- check that there is error handling for n/c type
            iterator += 3
        else:
            raise Exception("Program was terminated because it was missing '--create_random_graph arguments'. Requires 'n' (number of nodes) and 'c' (probability of an edge forming).")

        if iterator < end and args[iterator] == "--multi_BFS":
            remaining_args = args[iterator + 1:]

            for i in range(len(remaining_args)):
                if "--" not in remaining_args[i]:
                    multi_BFS_nodes.append(remaining_args[i])
                else:
                    iterator += i + 1
                    break
            
            if len(multi_BFS_nodes) == 0:
                raise Exception("Program was terminated because it was missing starting node(s) for the BFS analysis.")
            
            # TODO: call BFS from analysis: result = BFS(user_graph, multi_BFS_nodes)
        
        if iterator < end and args[iterator] == "--analyze":
            # TODO: call analysis from analysis: result = analysis(user_graph)
            iterator += 1
        
        if iterator < end and args[iterator] == "--plot":
            # TODO: call plot from visualization: result = visualization(user_graph)
            iterator += 1
        
        if iterator < end and args[iterator] == "--output":
            if iterator + 1 == end:
                raise Exception("Program was terminated because it was missing the output file name.")
            
            output_file = args[iterator + 1]
            iterator += 2
            # TODO: call file output from file_io: fio.save_graph(user_graph, output_file)
        
        if iterator < end:
            print("NOTE: extra arguments at the end of the input string were ignored:", args[iterator:])

main()
