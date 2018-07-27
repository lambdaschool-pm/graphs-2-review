#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Represent a vertex with a label and possible connected component."""

    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component
    
    def __repr__(self):
        return 'Vertex ' + self.label 

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
    
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices."""
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def dfs(self, start, target=None):
        """Search the graph using BFS or DFS."""
        stack = []
        stack.append(start)
        visited = set(stack)

        while stack:
            current = stack.pop() # pops the last one 

            # check if found target
            if current == target:
                return target 

            # add the current to the stack
            visited.add(current)

            # subtract whats visited from the vertices and whats remaining, add it to the stack
            stack.extend(self.vertices[current] - visited) 

        return visited

    def bfs(self, start, target=None):
        """Search the graph using BFS or DFS."""
        queue = []
        queue.append(start)
        visited = set(queue)
        
        while queue:
            current = queue.pop(0)  # pops the first one

            # check if found target
            if current == target:
                return target

            # add the current to the stack
            visited.add(current)

            # subtract whats visited from the vertices and whats remaining, add it to the stack
            queue.extend(self.vertices[current] - visited)

        return visited
    '''
    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        pass
    '''
    def find_components(self):
        """Identify components and update vertex component ids."""
        visited = set() 
        current_component = 0

        for vertex in self.vertices:
            # because you have been here so, you don't want to repeat
            if vertex not in visited:
                reachable = self.dfs(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components

