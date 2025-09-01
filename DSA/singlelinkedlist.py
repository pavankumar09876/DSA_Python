# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self,data):
#         new_node=Node(data)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
#         return data
#     def pop(self):
#         if self.head is None:
#             return None
#         temp=self.head
#         pre=self.head
#         while (temp.next):
#             pre=temp
#             temp=temp.next
#         self.tail=pre
#         self.tail.next=None
#         self.length-=1
#         if self.length==0:
#             self.tail=None
#         return temp.data
#     def prepend(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         new_node.next=self.head
#         self.head=new_node
#         self.length+=1
#         return data
#     def pop_first(self):
#         if self.head is None:
#             return None
#         temp=self.head
#         self.head=self.head.next
#         temp.next=None
#         self.length-=1
#         if self.length==0:
#             self.tail=None
#         return temp.data
#     def get(self,index):
#         if index<0 or index >= self.length:
#             return None
#         temp=self.head
#         for _ in range(index):
#             temp=temp.next
#         return temp.data
    
#     def set_value(self,index,data):
#         if index < 0 or index >= self.length:
#             return None
#         temp=self.head
#         for _ in range(index):
#             temp=temp.next
#         temp.data=data
#         return temp.data
    
#     def insert(self,index,data):
#         if index < 0 or index >= self.length:
#             return None
#         if index ==0:
#             return self.prepend(data)
#         if index >= self.length:
#             return self.append(data)
#         new_node=Node(data)
#         temp=self.head
#         for _ in range(index-1):
#             temp=temp.next
#         new_node.next=temp.next
#         temp.next=new_node
#         self.length+=1
#         return temp.data
    
#     def traverse(self):
#         if self.head is None:
#             return None
#         else:
#             temp=self.head
#             while temp:
#                 print(temp.data)
#                 temp=temp.next
# l=linkedlist(0)
# print("append is:",l.append(1))
# print("append is:",l.append(2))
# print("append is:",l.append(3))
# print("append is:",l.append(4))
# print("append is:",l.append(5))
# print("append is:",l.append(6))
# # print("pop item is:",l.pop())
# # print("prepend item is:",l.prepend(100))
# # print("pop_first item is:",l.pop_first())
# # print("get item is:",l.get(0))
# print("set value is:",l.set_value(2,200))
# print("insert value is:",l.insert(3,400))
# l.traverse()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,data):
        new_node=Node(data)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return data
    def prepend(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return data
    
    def pop(self):
        if self.head is None:
            return None
        temp=self.head
        pre=self.head
        while (temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        return temp.data
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        return temp.data
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return True
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.data
    
    def set_value(self,index,data):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.data=data
        return temp.data
    
    def insert(self,index,data):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        new_node=Node(data)
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return temp.data
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp=self.head
        for _ in range(index -1):
            temp=temp.next
        node_remove=temp.next
        temp.next=node_remove.next
        node_remove.next=None
        self.length-=1
        return temp.data  
    
    def traverse(self):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

    
l=linkedlist(0)
print("append is:",l.append(1))
print("append is:",l.append(2))
print("append is:",l.append(3))
print("append is:",l.append(4))
print("append is:",l.append(5))
print("append is:",l.append(6))
# print("pop item is:",l.pop())
# print("prepend item is:",l.prepend(100))
# print("pop_first item is:",l.pop_first())
# print("get item is:",l.get(0))
print("set value is:",l.set_value(2,200))
print("insert value is:",l.insert(3,400))
print("remove value:",l.remove(4))
l.traverse()
