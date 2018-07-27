import sys

# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight
#Vertex class
class Vertex:
    def __init__(self,value='vertex', color="white", parent=None):
        self.value = value
        self.edges = []
        self.color = color
        self.parent = parent 
 #Graph class

class Graph:
    def __init__(self):
        self.vertices = []
    

    '''
    * function looks through all the vertices in the graph and returns the
    * first one it finds that matches the value parameter.
    *
    * Used from the main code to look up the verts passed in on the command
    * line.
    *
    * @param: {*} value: The value of the Vertex to find
    *
    * @return None if not found.
    * return {Vertex} the found vertex
    * 
    '''
    def find_vertex(self, value):
        #!!! IMPLEMENT ME
        vert = [v for v in self.vertices if v.value == value]
        
        return vert[0]
        

    '''
    * Breadth-First search from a starting vertex. self should keep parent
    * pointers back from neighbors to their parent.
    *
    * @param:Vertex start The starting vertex for the BFS
    '''
    def bfs(self, start):
        """Search the graph using BFS or DFS."""
        start.color = 'gray'
        queue = [start]

        #init func already doing this
        """
        for vertex in self.vertices:
            vertex.color = 'white'
            vertex.parent = None
        """
        # refactor
        """
        start.color = 'gray'
        queue.append(start)
        """
        while queue:
          current = queue.pop(0)

          for edge in current.edges:
              vertex = edge.destination
              if vertex.color ==  'white':
                  vertex.color = 'gray'
                  vertex.parent = current
                  queue.append(vertex)

          current.color = 'black'

    '''
    * Print out the route from the start vert back along the parent
    * pointers(self,set in the previous BFS)
    *
    * @param:Vertex start The starting vertex to follow parent
    * pointers from
    '''
    def output_route(self, start):
      #!!! IMPLEMENT ME
        vertex = start
        output = ''

        while (vertex):
            output += vertex.value
            if (vertex.parent):
                output += ' --> '
            
            vertex = vertex.parent
        
        print(output)
    
    # Show the route from a starting vert to an ending vert.
    
    def route(self, start, end):
        #Do BFS and build parent pointer tree
        self.bfs(end)

        #Show the route from the start
        self.output_route(start)

# Helper function to add bidirectional edges
def add_edge(v0, v1):
    v0.edges.append(Edge(v1))
    v1.edges.append(Edge(v0))


#Main


"""
```
pseudocode
BFS(graph, startVert):
  for v of graph.vertices:
    v.color = white
    v.parent = null // <-- Add parent initialization

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        v.parent = u // <-- Keep a parent link
        queue.enqueue(v)

    queue.dequeue()
    u.color = black
```

## Procedure

1.  Perform a BFS from the _ending vert_(host). self will set up all the
    `parent` pointers across the graph.

2.  Output the route by following the parent pointers from the _starting_ vert
    printing the values as you go.

## Sample Run

```
$ node routing.js HostA HostD
HostA - -> HostB - -> HostD
$ node routing.js HostA HostH
HostA - -> HostC - -> HostF - -> HostH
$ node routing.js HostA HostA
HostA
$ node routing.js HostE HostB
HostE - -> HostF - -> HostC - -> HostA - -> HostB
```
"""
