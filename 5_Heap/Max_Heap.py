import heapq

class max_heap:
    def __init__(self):
        self.heap=[]

    def insert(self,value):
        heapq.heappush(self.heap, -value)

    def get_max(self):
        if self.heap is not None:
            return -self.heap[0] 
        return "heap is empty"
        
    def pop_max(self):
        return -heapq.heappop(self.heap) if self.heap else None 

    def view_maxheap(self):
        return("Max_heap :",[-value for value in self.heap])
    
l=max_heap()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print("get min:",l.get_max())
print("view heap:",l.view_maxheap())
print("pop minheap:",l.pop_max())
print("view heap:",l.view_maxheap())
