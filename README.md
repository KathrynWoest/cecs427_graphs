# CECS 427 Project 1: Graphs
Completed By: Kathryn Woest (030131541) and Grace Flores ()


## Usage Instructions
**NOTE: `plot.py` relies on a command that is not compatible with WSL. This command automatically opens up the graph's visualizations. If you are unable to use a different terminal like Powershell, comment out `plot.py`'s line 136: `webbrowser.open("graph.html")` and manually open the generated `.html` files through your file explorer.

1. Clone this repo and open it on your IDE

2. DEPENDENCIES: This program relies on two external libraries, which were cleared by the professor. To install them, ensure you are inside the project directory and run these commands:
    1. **NetworkX**, a library that provides `.gml` file parsing and writing, graph support, and analysis functions. To install, run: `pip install networkx[default]`
    2. **Pyvis**, a library that provides graph plotting. To install, run: `pip install pyvis`

3. Run this program with: `python graph.py --input input_file.gml --create_random_graph n c --multi_BFS a1 a2 ... --analyze --plot --output output_file.gml`
    1. `--create_random_graph` will override the `--input` command and use a generated graph over the provided file's graph
    2. All arguments can be provided in any order. For example, `python graph.py --input input_file.gml --plot --analyze` will return the same results as `python graph.py --plot --analyze --input input_file.gml`
    3. However, parameters to those arguments must follow the arguments. For example, `--multi_BFS` MUST be directly followed by all the starting nodes `a1, a2, ...` or they will be skipped and the program will throw an exception
    4. With the exception of `--input` or `--create_random_graph`, all other commands are optional. For example, you could just generate and analyze a graph with no plotting, BFS searches, or writing to an output files


## Implementation Description
1. **Overall Program:** `graph.py` will read in or generate a graph, then check for arguments that call for BFS_searches, analysis, plotting, or writing to an output file in that order (even if they are in a different order in the `python graph.py` command)
2. **graph.py:** `graph.py` checks for missing arguments and calls the necessary modules to execute the arguments. Although the usage of `if --command in args` is not the most efficient, the argument list will never be large enough for that to be an issue. Additionally, this allows for commands to be in any order and still be executed properly. Uses error handling to address missing arguments (including parameters to commands like the file names, n, c, a1, etc). Utilizes `if elif else` statements to iterate through possible commands and to properly call functions like `plot()` and `save_graph()` based on what analysis was completed
3. **file_io.py:** 
4. **generator.py:** 
5. **analyze.py:** 
6. **plot.py:**


## Example Commands and Outputs