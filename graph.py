import sys

def main():
    args = sys.argv

    # Will decide later, but might switch these in the program just to actually calling necessary functions lol

    generate = False
    multi_BFS = False
    multi_BFS_nodes = []
    analyze = False
    plot = False
    output = False

    iterator = 1
    end = len(args)

    if end < 3:
        pass  # raise an error, not enough arguments to do anything
    
    else:
        if args[1] == "--input":
            input_file = args[2]
            iterator += 2
        elif end > 3 and args[1] == "--create_random_graph":
            generate = True
            n = args[2]
            c = args[3]
            iterator += 3
        else:
            pass  # raise an error and quit program, missing argument and have no graph

        if iterator < end and args[iterator] == "--multi_BFS":
            remaining_args = args[iterator + 1:]
            multi_BFS = True

            for i in range(len(remaining_args)):
                if "--" not in remaining_args[i]:
                    multi_BFS_nodes.append(remaining_args[i])
                else:
                    iterator += i + 1
                    break
            
            if len(multi_BFS_nodes) == 0:
                pass  # raise error, no nodes to start BFS with
        
        if iterator < end and args[iterator] == "--analyze":
            analyze = True
            iterator += 1
        
        if iterator < end and args[iterator] == "--plot":
            plot = True
            iterator += 1
        
        if iterator < end and args[iterator] == "--output":
            output = True
            # check if output file exists before calling this
            output_file = args[iterator + 1]

main()
