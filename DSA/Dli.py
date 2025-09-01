class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Double_linked_list:
    def __init__(self,data):
        new_node=Node(data)
        self.head=new_node
        self.tail=new_node
        self.length=1
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
        return data
    # def pop(self):
    #     if self.length==0:
    #         return None
    #     else:
    #         temp=self.tail
    #         self.tail=self.tail.prev
    #         self.tail.next=None
    #         temp.prev=None
    #     self.length-=1
    #     if self.length == 1:
    #         self.head=None
    #         self.tail=None
    #     return temp.data
    def pop(self):
        if self.length==0:
            return "Pavan"
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
        if self.head is None:
            return None
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return data
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head.next=self.head
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
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.data=value
            return True
        return False
    
    def insert(self,index,data):
        if index<0 or index> self.length:
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

    
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
l=Double_linked_list(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.prepend(60)
l.prepend(70)
l.prepend(80)
# print("Pop item is:",l.pop())
# # print("Pop item is:",l.pop())
# # print("Pop item is:",l.pop())
# # print("Pop item is:",l.pop())
# print("pop_first is:",l.pop_first())
# print("get iem is:",l.get(2))
l.set_value(1,100)
l.insert(2,300)
l.traverse()