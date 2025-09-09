# class Heap:
#     def __init__(self):
#         self.heap=[]
#     def _leftchild(self,index):
#         return 2 * index +1
#     def _rightchild(self,index):
#         return 2 * index +2
#     def _parent(self,index):
#         return (index-1)//2
#     def swapcase(self,index1,index2):
#         self.heap[index1],self.heap[index2] = self.heap[index1],self.heap[index2]

#     def insert(self,value):
#         self.heap.append(value)
#         self._heapify_up(len(self.heap)-1)
    
#     def _heapify_up(self,index):
#         parent = self._parent(index)
#         while index > 0 and self.heap[index] > self.heap[parent]:
#             self.swapcase(index,parent)
#             index=parent
#             parent=self._parent(index)
    
#     def __str__(self):
#         return str(self.heap)


# h = Heap()
# h.insert(10)
# h.insert(5)
# h.insert(20)
# h.insert(3)
# print("Heap:", h)



import heapq

class Min_heap:
    def __init__(self):
        self.heap=[]

    def insert(self,value):
        heapq.heappush(self.heap,value)

    def get_min(self):
        if self.heap is not None:
            return self.heap[0] 
        else:
            return "heap is empty"
        
    def pop_min(self):
        return heapq.heappop(self.heap) if self.heap else None 

    def view_minheap(self):
        return self.heap
    
l=Min_heap()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
print("get min:",l.get_min())
print("view heap:",l.view_minheap())
print("pop minheap:",l.pop_min())
print("view heap:",l.view_minheap())