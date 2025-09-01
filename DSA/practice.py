class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self): 
        self.head=None
        self.tail=None
        self.length=0
    def append(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
    def prepend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def pop(self):
        if self.length==0:
            raise Exception("List is empty")
        temp=self.head
        pre=self.head
        while (temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.data
    def pop_first(self):
        if self.length==0:
            raise Exception("List is Empty")
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length+=1
        if self.length==0:
            self.tail=None
        return temp.data
    
    
ll = linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

print(ll.pop())   # 30
print(ll.pop())   # 20
# print(ll.pop_first())   # 5
# print(ll.pop())   # None
