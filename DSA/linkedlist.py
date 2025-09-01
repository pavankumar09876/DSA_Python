class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
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
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
    def prepand(self,data):
        new_node=Node(data)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            print("Empty")
        temp=self.head
        self.head.next=self.head
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.data

    #Remove given value from linked list
    def remove(self, value):
        if self.head is None:
            print("List is empty")
            return
    # If the head node holds the value
        if self.head.val == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.val == value:
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Value not found in the list")

    
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    

    
linkedlist1=linkedlist(4)
linkedlist1.append(10)
linkedlist1.append(20)
linkedlist1.append(30)
linkedlist1.prepand(3)
# linkedlist1.pop()
linkedlist1.display()
# print("Head",linkedlist1.head.value)
# print("Tail",linkedlist1.tail.value)
# print("Length",linkedlist1.length)
