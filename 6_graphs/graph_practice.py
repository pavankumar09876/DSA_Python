class Graph:
    def __init__(self):
        self.adj_list={}
    
    def add_vertex(self,vertex):
        if vertex in self.adj_list:
            return f"{vertex} is already present"
        else:
            self.adj_list[vertex]=[]
        return vertex
    
    def add_edjes(self,v1,v2):
        if v1 in self.adj_list or v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        else:
            return f"{v1,v2} not in self.adj_list"
        
    def remove_edjes(self,v1,v2):
        if v1 not in self.adj_list or v2 not in self.adj_list:
            try:
                self.adj_list[v1].remove[v2]
                self.adj_list[v2].remove[v1]
            except ValueError:
                pass
        return v1,v2

    def remove_vertex(self,vertex):
        if vertex not in self.adj_list[vertex]:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
        return f"{vertex} not in self.adj_list"

l=Graph()
l.add_vertex(1)
l.add_vertex(2)
l.add_vertex(3)
l.add_vertex(4)
l.add_vertex(5)
l.add_edjes(1,2)
l.add_edjes(1,3)
l.add_edjes(2,3)
l.add_edjes(3,4)
print(l.adj_list)
# l.add_edges(4,5)
l.remove_vertex(4)
# l.remove_edjes(4,5)
print(l.adj_list)  
