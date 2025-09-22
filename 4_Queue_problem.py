# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class queue:
#     def __init__(self):
#         self.top=None
#         self.bottom=None
#         self.length=0
    
#     def enqueue(self,value):
#         new_node=Node(value)
#         if self.top is None:
#             self.top=new_node
#         else:
#             new_node.next=self.top
#             self.top=new_node
#         self.length+=1
    
#     def dequeue(self):
#         if self.top is None:
#             return None
#         else:
#             temp=self.top
#             pre=self.top
#             while temp.next:
#                 pre=temp
#                 temp=temp.next
#             self.bottom=pre
#             self.bottom.next=None
#         self.length-=1
#         return pre.value
    



#     def view_queue(self):
#         if self.top is None:
#             return None
#         else:
#             temp=self.top
#             while temp:
#                 print(temp.value,end=" -> ")
#                 temp=temp.next
#             print("none")

# l=queue()
# for i in [1,2,3,4,5,6,7]:
#     l.enqueue(i)
# l.view_queue()
# print("dequeue is:",l.dequeue())
# l.view_queue()



# Implement Queue using Stacks


class Myqueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,values):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(values)
       # print(self.stack1,end=" - ")

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return self.stack1
    

    def dequeue(self):
        if not self.stack1:
            return "nothing in stack1"
        return self.stack1.pop()
    
    def peek(self):
        if not self.stack1:
            return "nothinf to peek"
        return self.stack1[-1]    

    def is_empty(self):
        return len(self.stack1) == 0

   
l=Myqueue()
print(l.is_empty())
for i in [1,2,3,4,5]:
    l.enqueue(i)

# l.enqueue(1)
# l.enqueue(2)
# l.enqueue(3)
# l.enqueue(4)
print(l.stack1)
print("peek:",l.peek())
print("dequeue:",l.dequeue())
print("peek:",l.peek())
print(l.stack1)
print(l.is_empty())
