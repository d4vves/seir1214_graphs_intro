class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = []

    def __str__(self):
        edges = []
        for vertex in self.edges:
            edges.append(vertex.data)
        return f'{self.data}: {edges}'

    def add_edge(self, vertex):
        if vertex not in self.edges:
            self.edges.append(vertex)

class Graph():
    def __init__(self):
        self.vertices = []

    def __str__(self):
        vertex_dict = {}
        for vertex in self.vertices:
            edges = []
            for edge in vertex.edges:
                edges.append(edge.data)
            vertex_dict[vertex.data] = edges
        return str(vertex_dict)


    def add_vertex(self, vertex):
        if vertex.data not in self.vertices:
            self.vertices.append(vertex)
        else:
            return 'Vertex exists!'

    def add_connection(self, start, end):
        if start in self.vertices and end in self.vertices:
            for vertex in self.vertices:
                if vertex.data == start.data:
                    vertex.add_edge(end)

    def find_path(self, start, end, path = []):
        path = path + [start.data]
        if start.data == end.data:
            return path
        for vertex in self.vertices:
            if vertex.data == start.data:
                for edge in vertex.edges:
                    if edge.data not in path:
                        new_path = self.find_path(edge, end, path)
                        return new_path
    

v1 = Vertex('Dave')
v2 = Vertex('Taylor')
v3 = Vertex('Trisha')
v4 = Vertex('Jason')
v5 = Vertex('Patrick')

graph = Graph()

graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex(v4)
graph.add_vertex(v5)

graph.add_connection(v1, v5)
graph.add_connection(v1, v3)
graph.add_connection(v5, v3)
graph.add_connection(v3, v4)
graph.add_connection(v4, v2)
graph.add_connection(v5, v4)

print(graph.find_path(v1, v2))
