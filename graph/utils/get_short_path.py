def breadth_first_search(graph: dict, start: str, goal: str) -> dict:
    """Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]),
    and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth
    level.
    Reference link :- https://en.wikipedia.org/wiki/Breadth-first_search
    Args:
        graph (dict): graph
        start (chr): start node
        goal (chr): goal node

    Returns:
        str: [description]
    """
    visited = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        return {"success": False, "message": "Same Node"}

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in visited:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    return {"success": True, "path": ", ".join(map(str, new_path))}
            visited.append(node)

    # Condition when the nodes
    # are not connected
    return {
        "success": False,
        "message": f"So sorry, but a connecting -> {start,goal} <- path doesn't exist",
    }
