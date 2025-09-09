class Graphs:
    def __init__(self):
        self.adjacency_list= { }
        
    def add_vertex(self,vertice):
        if  vertice in self.adjacency_list:#.keys() :
            return f"{vertice} Duplicate vertices are Not allow"
        else:
            self.adjacency_list[vertice]=[]
            return self

    def add_edges(self,vertex1,vertex2):
        if vertex1  in self.adjacency_list or vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
        return self

    def remove_edjes(self,vertex1,vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
        return self
    
    # def remove_vertex(self,vertex1,vertex2):
    #     if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
    #         raise Exception("Vertex is not present")
    #     self.adjacency_list[vertex1].remove(vertex2)
    #     self.adjacency_list[vertex2].remove(vertex1)
    #     return self

    def remove_vertex(self,vertex):
        if vertex not in self.adjacency_list[vertex]:
            for othre_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[othre_vertex].remove(vertex)
            del self.adjacency_list[vertex]
        return self

l=Graphs()
l.add_vertex(1)
l.add_vertex(2)
l.add_vertex(3)
l.add_vertex(4)
l.add_vertex(5)
l.add_edges(1,2)
l.add_edges(1,3)
l.add_edges(2,3)
l.add_edges(3,4)
print(l.adjacency_list)
# l.add_edges(4,5)
l.remove_vertex(4)
# l.remove_edjes(4,5)
print(l.adjacency_list)