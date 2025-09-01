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
        if self.head is None:
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
        return True
    def pop(self):
        if self.head is None:
            return None
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None

    def pop_first(self):
        if self.head is None:
            return "EMpty"
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.data
    def get(self,index):
        if index < 0 or self.length >= index:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp
                
    def display(self):
        if self.head is None:
            raise Exception("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
l=linkedlist()
l.append(1)
l.append(2)
l.prepend(3)
l.prepend(4)
l.prepend(5)
l.prepend(6)
remove=l.pop_first()
print("Removed:",remove)
print(l.get(2))
l.display()