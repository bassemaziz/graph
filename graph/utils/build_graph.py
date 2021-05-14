from collections import defaultdict


def build_graph(edges: list) -> dict:
    """Function to build the graph

    Args:
        edges (list): edges

    Returns:
        dict: Dictinary
    """
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph
