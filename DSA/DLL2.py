# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Double_linked_list:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.length=0
        
#     def append(self,data):
#         new_node=Node(data)
#         if self.length==0:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             new_node.prev=self.tail
#             self.tail=new_node
#         self.length+=1

#     def pop(self):
#         if self.length==0:
#             return None
#         temp=self.tail
#         if self.length==1:
#             self.head=None
#             self.tail=None
#         else:
#             self.tail=self.tail.prev
#             temp.prev=None
#             self.tail.next=None
#         self.length-=1
#         return temp.data

#     def prepend(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             new_node.next=self.head
#             self.head.prev=new_node
#             self.head=new_node
#         self.length+=1
#         return data
    
#     def traverse(self):
#         if self.length==0:
#             return "Pavan"
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next


# l=Double_linked_list()
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# print("Pop item is:",l.pop())
# print("Pop item is:",l.pop())
# print("Prepend item is:",l.prepend(7))
# l.traverse()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            temp.prev=None
            self.tail.next=None
        self.length-=1
        return temp.data

    def prepend(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp.data
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return "Get None"
        if index < self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp

    # def insert(self,index,data):
    #     if index<0 or index> self.length:
    #         return None
    #     if index==0:
    #         return self.prepend(data)
    #     if index== self.length:
    #         return self.append(data)
        
    #     new_node=Node(data)
    #     before=self.get(index-1)
    #     after=before.next

    #     new_node.prev=before
    #     new_node.next=after
    #     before.next=new_node
    #     after.prev=new_node
    #     self.length+=1
    #     return True

    def insert(self,index,data):
        if index < 0 or index > self.length:
            return None
        if index==0:
            return self.prepend(data)
        if index==self.length:
            return self.append(data)
        new_node=Node(data)
        before=self.get(index-1)
        after=before.next

        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp=self.get(index)
        # before=temp.prev
        # after=temp.next
        # before.next=after
        # after.prev=before
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None
        return temp.data
    
    
    def traverse(self):
        if self.length==0:
            return "Empty"
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
l=dlinkedlist()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.prepend(6)
print("pop is:",l.pop())
print("Pop_first is:",l.pop_first())
l.get(2)
l.insert(1,40)
print("Remove is:",l.remove(3))
l.traverse()
    

