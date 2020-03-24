import networkx as nx
import matplotlib.pyplot as plt
import random

# Here, the graph will be a dictionnay with the name of the node as key, and a list of all connected node as value
# Ex: {'1': ['2', '3'], '2': ['1'], '3': ['1']}

def build_line_graph(graph, generateGraph):
    new_graph = dict({})
    if generateGraph == True:
        G = nx.Graph()
    for key in graph:
        if generateGraph == True:
            G.add_node(key)
        for node in graph[key]:
            if generateGraph == True:
                G.add_edge(key, node)
                new_node = key + '-' + node
                reversedKey = node + '-' + key
                if reversedKey in new_graph:
                    new_node = reversedKey
                else:
                    new_graph[new_node] = []
                for othersNode in graph[key]:
                    if node != othersNode:
                        new_otherNode = key + '-' + othersNode
                        if (othersNode + '-' + key) in new_graph:
                            new_otherNode = othersNode + '-' + key
                        new_graph[new_node].append(new_otherNode)
    if generateGraph == True:
        for key in new_graph:
            G.add_node(key)
            for node in new_graph[key]:
                G.add_edge(key, node)
        # set available colors
        available_node_colors = ["#46b2e0", "#cbe046", "#a246e0", "#e8a264"]
        available_edges_colors = ["#e8d464", "#b1e864", "#64a8e8", "#1c6fbd"]

        # set random node colors
        node_colors = list()
        node_sizes = list()
        for node in G.nodes:
            node_colors.append(random.choice(available_node_colors))
            node_sizes.append(random.uniform(50, 400))

        # set random edges colors
        edge_colors = list()
        edge_widths = list()
        for edge in G.edges:
            edge_colors.append(random.choice(available_edges_colors))
            edge_widths.append(random.uniform(0.2, 2.5))

        nx.draw(G,
            node_size=node_sizes,
            node_color=node_colors,
            edge_color=edge_colors,
            width=edge_widths,
            with_labels=True)
        plt.show()
    return new_graph