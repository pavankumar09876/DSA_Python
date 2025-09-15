class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return "Get None"
        if index < self.length//2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length,index,-1):
                temp=temp.prev
        return temp
    
    def insert(self,index,value):
        new_node=Node(value)
        if index == 0:
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            self.length+=1

            if index == self.length:
                return self.append(value)
        
        before=self.get(index-1)
        after=before.next
        new_node.next=after
        new_node.prev=before
        before.next=new_node
        after.prev=new_node
        self.length+=1

    # 3. Insert at index (0..length)
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        # cur is node currently at index
        new_node = Node(value)
        prev = temp.prev
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        temp.prev = new_node
        self.length += 1
        return True

    def delete_by_value(self, key):
        temp = self.head
        while temp:
            if temp.value == key:

                if temp.prev is not None:
                    # temp.prev.next = temp.next
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
                else:
                    self.head = temp.next

                if temp.next is not None:
                    # temp.next.prev = temp.prev
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
                return
            temp = temp.next
        return temp

    def middle_node(self):
        if self.head is None:
            return None
        temp=self.head
        for _ in range(self.length//2):
            temp=temp.next
        return temp.value
    
    def middle_value(self):
        if self.head is None:
            return None
        slow=self.head
        fast=self.head
        while fast:
            slow=slow.next
            fast=fast.next.next
        return slow.next
    
    def remove_d(self):
        seen=set()
        temp=self.head
        previous=self.head
        while temp:
            if temp.value == seen:
                if temp.prev:
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
                else:
                    self.head=temp.next
                if temp.next:
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
            else:
                seen.add(temp.value)
            temp=temp.next
        return seen

    def remove_duplicates(self):
        temp=self.head
        while temp and temp.next:
            if temp.value == temp.next.value:
                temp.next=temp.next.next
            else:
                temp=temp.next

    def remove_duplicates_reverse(self):
        temp=self.tail
        while temp and temp.prev:
            if temp.value == temp.prev.value:
                temp.prev=temp.prev.next
            else:
                temp=temp.prev

    def remove_occurence(self,key):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            if temp.value == key:
                if temp.prev:
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
                else:
                    self.head=temp.next
                if temp.next:
                    before=temp.prev
                    after=temp.next
                    before.next=after
                    after.prev=before
                else:
                    self.tail=temp.prev
            temp=temp.next


    def find_key_index(self,key):
        temp=self.head
        index=0
        while temp:
            if temp.value == key:
                return index
            temp=temp.next
            index+=1
        return -1


    def count_nodes(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

    def reverse(self):
        if self.head is None and self.head.next is None:
            return None
        temp=self.head
        while temp:
            temp.next,temp.prev=temp.prev,temp.next
            temp=temp.prev
        self.head,self.tail=self.tail,self.head

    def split_list(self):
        if self.head is None:
            return None
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        if second_half is not None:
            second_half.prev=None
        return None

    

    def traverse_forward(self):
        if self.length==0:
            return "Empty"
        else:
            temp=self.head
            while temp:
                print(temp.value,end=" <-> ",)
                temp=temp.next
            print("none")
    
    def traverse_backward(self):
        if self.head is None:
            return None
        temp=self.tail
        while temp:
            print(temp.value,end=" <=> ")
            temp=temp.prev
        print("none")

l=dlinkedlist()
l = dlinkedlist()
for v in [1,1,2,3,3,3,3,4,5,5,6,7,7]:
    l.append(v)
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(5)
# l.append(6)
# l.append(7)
l.traverse_forward()
# print("insert",l.insert(2,99))
# print(l.delete_by_value(3))
print(l.remove_d())
# print("remove_duplicate:",l.remove_duplicates())
# l.remove_occurence(3)
# print("count nodes:",l.count_nodes())
# print("find key:",l.find_key(6))
# l.reverse()
# l.split_list()
# l.traverse_backward()
l.traverse_forward()

