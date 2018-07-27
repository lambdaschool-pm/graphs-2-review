def bfs(self, start, target=None):
    queue = [start]
    visited = set()
    while queue:
        :
        current = queue.pop(0)
        if current == target:
            break
        visited.add(current)
        # Add possible (unvisited) vertices to queue
        queue.extend(self.vertices[current] - visited)

    return visited


def dfs(self, start, target=None):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current == target:
            break
        visited.add(current)
        # Add possible (unvisited) vertices to queue
        stack.extend(self.vertices[current] - visited)

    return visited


def search(self, start, target=None, method='dfs'):
    quack = [start]
    pop_index = 0 if method == 'bfs' else -1
    visited = set()
    while quack:
        current = stack.pop(pop_index)
        if current == target:
            break
        visited.add(current)
        # Add possible (unvisited) vertices to queue
        quack.extend(self.vertices[current] - visited)

    return visited
