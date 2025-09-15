class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class single_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def traverse(self):
        if self.head is None:
            return "nothing to traverse"
        else:
            temp=self.head
            while temp:
                print(temp.value,end=" -> ")
                temp=temp.next
            print("none")
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    
    def pop(self):
        if self.head is None:
            return "Nothing to pop"
        temp=self.head
        pre=self.head
        while temp.next:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        return temp.value
    
    def pop_first(self):
        if self.head is None:
            return "Nothing to pop first"
        else:
            temp=self.head
            self.head.next=self.head
            temp.next=None
        self.length-=1
        return temp
    
    def get_value(self,value):
        if self.head is None:
            return "List is empty"
        temp=self.head
        while temp:
            if temp.value == value:
                return temp.value
            temp=temp.next
        return False
    
    def get_value_index(self,index):
        if index < 0 or index > self.length:
            return "out of bound"
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.value
            
    
    def set_value(self,value,index):
        if index < 0 or index > self.length:
            return "Out of bound"
        temp=self.head
        for _ in range(index):
            temp=temp.next
        temp.value=value
        return temp.value
    
    def insert(self,value,index):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        if index == self.length:
            return self.append(value)
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return temp.value
    
    def remove_value_by_index(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        temp=self.head
        for _ in range(index-1):
            temp=temp.next
        removed_node=temp.next
        # temp.next=removed_node
        # removed_node.next=None
        
        temp.next=removed_node.next
        removed_node.next=None
        self.length-=1
        return temp.value
    
    def remove_value(self,value):
        if self.head is None:
            return "list is empty"
        temp=self.head
        if self.head.value==value:
            self.head=self.head.next
            return "removed"
        while temp.next:
            if temp.next.value == value:
                temp.next=temp.next.next
                return f"{value} removerd"
            temp=temp.next
        

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        after=temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

    def mid_value(self):
        if self.head is None:
            return None
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.value
    
    def has_loop(self):
        if self.head is None:
            return None
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
            return False
        
    def remove_duplicates(self):
        if self.head is None:
            return None
        seen=[]
        temp=self.head
        while temp:
            if temp.value in seen:
                temp.next=temp.next.next
            else:
                seen.append(temp.value)
            temp=temp.next
        return seen            


l=single_linked_list()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(4)
l.append(4)
l.append(5)
l.append(6)
l.prepend(7)
l.prepend(8)
l.traverse()
# print(l.remove_value(4))
# l.pop()
# l.pop_first()
# l.get_value(5)
# print(l.get_value_index(3))
# print(l.set_value(99,4))
# print(l.insert(100,3))
# print(l.remove_value_by_index(5))
# l.reverse()
# print(l.mid_value())
# l.tail=l.head
# print(l.has_loop())
print(l.remove_duplicates())
l.traverse()
       
    
