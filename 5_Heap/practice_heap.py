import heapq
class Min_heap:
    def __init__(self):
        self.heap=[]
    
    def insert(self,value):
        return heapq.heappush(self.heap,value)
    
    def get_minheap(self):
        if self.heap is not None:
            return self.heap[0]
        return "Heap is empty"
    
    def pop_min(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def view_heap(self):
        return self.heap
    
l=Min_heap()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print("get min:",l.get_minheap())
print("view heap:",l.view_heap())
print("pop minheap:",l.pop_min())
print("view heap:",l.view_heap())
print("---------------")

class Max_heap:
    def __init__(self):
        self.heap=[]
    
    def insert(self,value):
        return heapq.heappush(self.heap,-value)
    
    def get_maxheap(self):
        if self.heap is not None:
            return -self.heap[0]
        return "Max_heap is empty"
    
    def max_pop(self):
        return -heapq.heappop(self.heap)
    
    def view_heap(self):
        return [-value for value in self.heap]

l=Max_heap()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print("get max:",l.get_maxheap())
print("view heap:",l.view_heap())
print("pop maxheap:",l.max_pop())
print("view heap:",l.view_heap())