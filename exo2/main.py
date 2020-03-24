import lineGraph    


my_graph = {
    '1': ['2', '3', '6'], 
    '2': ['1'],
    '3': ['1', '6'],
    '6': ['1', '3', '8'],
    '7': ['8'],
    '8': ['7', '6']
}
res = lineGraph.build_line_graph(my_graph, True)
