def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of lists): A list of boxes, where each box contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    def dfs(box_index):
        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key)

    n = len(boxes)
    visited = [False] * n  # Track whether a box has been visited
    dfs(0)  # Start DFS traversal from the first box

    return all(visited)
