maze = \
[['+', '-', '+', '-', '+', '-', '+'],
['|', ' ', ' ', ' ', ' ', ' ', '|'],
['+', ' ', '+', '-', '+', ' ', '+'],
['|', ' ', ' ', 'F', '|', ' ', '|'],
['+', '-', '+', '-', '+', ' ', '+'],
['|', '$', ' ', ' ', ' ', ' ', '|'],
['+', '-', '+', '-', '+', '-', '+']]

def parse_maze():
    start, end, paths = None, None, []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == ' ':
                paths.append((i, j))
            if maze[i][j] == '$':
                paths.append((i, j))
                start = (i, j)
            if maze[i][j] == 'F':
                paths.append((i, j))
                end = (i, j)
    return start, end, paths

def bfs_maze_solver(start, end, walkable):
    # Create a queue for BFS
    queue = []
    # Mark the start position as visited and enqueue it
    queue.append(start)
    # Create a dictionary to store the parent of each position
    parent = {}
    # Mark all other positions as unvisited
    visited = set()
    # While queue is not empty
    while queue:
        # Dequeue a position from queue
        pos = queue.pop(0)
        # If the position is the destination, we are done
        if pos == end:
            break
        # Otherwise, mark it as visited
        visited.add(pos)
        # Get all adjacent positions
        adjacent = get_adjacent(pos, walkable)
        # For each adjacent position
        for a in adjacent:
            # If it is not visited
            if a not in visited:
                # Mark it as visited
                visited.add(a)
                # Enqueue it
                queue.append(a)
                # Store its parent
                parent[a] = pos
    # Generate the path from start to end
    path = []
    pos = end
    while pos != start:
        path.append(pos)
        pos = parent[pos]
    path.append(start)
    # Reverse the path
    path.reverse()
    # Return the path
    return path

def get_adjacent(pos, walkable):
    # Get the x and y coordinates
    x, y = pos
    # Create a list of adjacent positions
    adjacent = []
    # Check if the position to the left is walkable
    if (x-1, y) in walkable:
        adjacent.append((x-1, y))
    # Check if the position to the right is walkable
    if (x+1, y) in walkable:
        adjacent.append((x+1, y))
    # Check if the position above is walkable
    if (x, y-1) in walkable:
        adjacent.append((x, y-1))
    # Check if the position below is walkable
    if (x, y+1) in walkable:
        adjacent.append((x, y+1))
    # Return the list of adjacent positions
    return adjacent

def direction(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    if y2 > y1:
        return "right"
    if y2 < y1:
        return "left"
    if x2 > x1:
        return "down"
    if x2 < x1:
        return "up"

start, end, paths = parse_maze()
route = bfs_maze_solver(start, end, paths)
formatted = []
for node1, node2 in zip(route, route[1:]):
    formatted.append(direction(node1, node2))
print(", ".join(formatted))
