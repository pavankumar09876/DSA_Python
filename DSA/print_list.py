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

    def prepend(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
       
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
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
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    # def set_value(self,index,data):
    #     temp=self.get(index)
    #     if temp:
    #         temp.data=data
    #         return True
    #     return False

    def set_value(self,index,data):
        if index < 0 or index >= self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.data=data
        return temp.data

    # def insert(self,index,data):
    #     new_node=Node(data)
    #     # if index < 0 or index > self.length:
    #     #     return False
    #     if index == 0:
    #         new_node.next=self.head
    #         self.head=new_node
    #     else:
    #         temp=self.head
    #         pre=None
    #         count =0
    #         while temp is not None and count < index:
    #             pre=temp
    #             temp=temp.next
    #             count+=1
    #         new_node.next=temp
    #         pre.next=new_node
    #     self.length+=1
    #     return True

    def insert(self, index, data):
        if index < 0 or index > self.length:   # out of bounds
            return False
        if index == 0:                         # insert at head
            return self.prepend(data)
        if index == self.length:               # insert at tail
            return self.append(data)

        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):             # stop at node before index
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index<0 or index >= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp.data
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

    
    
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
l=linkedlist()
# n=Node(10)
# l.head=n
# n1=Node(20)
# l.head.next=n1
# n2=Node(30)
# n1.next=n2
# l.tail=n2
# l.length=3

l.append(40)
l.append(50)
l.append(60)
# l.pop()
l.prepend(1)
# l.pop_first()
# print(l.get(4))
l.insert(1,67)
# print(l.set_value(1,59))
# l.remove(2)
l.reverse()
l.display()
