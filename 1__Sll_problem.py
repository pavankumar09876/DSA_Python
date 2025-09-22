class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class singlelinkedlist:
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
            self.tail=new_node
        self.length+=1
    
    def get_value_by_index(self,index):
        if index < 0 or index >= self.length:
            return "out bound"
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.value

    def middle_value(self):
        if self.head is None:
            return None
        temp=self.head
        for i in range(self.length//2):
            temp=temp.next
        return temp.value
    #  Another method using get
        # i=self.length//2
        # return self.get_value(i)

   # without length
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return f"{slow.value} cycle detected"
        return "no cycle involved"
            
    def k_th_value(self,k):
        return self.get_value(self.length - k)
    
    def remove_duplicate(self):
        seen=set()
        temp=self.head
        previous=self.head
        while temp:
            if temp.value in seen:
                previous.next=temp.next
            else:
                seen.add(temp.value)
            temp=temp.next
        return seen
    
    def remove_duplicate_sortedlist(self):
        if self.head is None:
            return None
        temp=self.head
        while temp and temp.next:
            if temp.value == temp.next.value:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return self
    
    #give only values
    def odd_even(self):
        odd=[]
        even=[]
        temp=self.head
        index =0
        while temp:
            if temp.value % 2==0:
                even.append(temp.value)
            else:
                odd.append(temp.value)
            temp=temp.next
            index+=1
        return odd,even
    
    # gives index and value
    def odd_even(self):
        odd=[]
        even=[]
        temp=self.head
        index =0
        while temp:
            if temp.value % 2==0:
                even.append(temp.value)
            else:
                odd.append(temp.value)
            temp=temp.next
            index+=1
        return odd,even

    def get_nth_node(self,n_index):
        if n_index<= 0:
            return None
        temp=self.head
        count=0
        while temp:
            if count == n_index:
                return temp.value
            temp=temp.next
            count+=1

    def nth_value_end(self,n):
        if n <= 0 or n > self.length:
            return None
        fast=self.head
        slow=self.head
        for _ in range(n):
            fast=fast.next
        while fast is not None:
            slow=slow.next
            fast=fast.next
        return slow.value
    


    # def merge_sorted_lists(self,l1, l2):
    #     dummy = Node(0)   # Temporary start node
    #     self.tail = dummy

    #     while l1 and l2:
    #         if l1.value <= l2.value:
    #             tail.next = l1
    #             l1 = l1.next
    #         else:
    #             tail.next = l2
    #             l2 = l2.next
    #         tail = tail.next

    #     # Attach the remaining part
    #     if l1:
    #         tail.next = l1
    #     else:
    #         tail.next = l2
    #     return dummy.next
    
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
        

    def sum_linked_list(self):
        if self.head is None:
            return None
        temp=self.head
        total=0
        while temp:
            total+=temp.value
            temp=temp.next
        return total

    def binary_decimal(self):
        num=0
        current=self.head
        while current:
            num=num*2 + current.value      #2,10,16
            current=current.next
        return num
    
    # def merge_two_sorted(self,l1,l2):
    #     dummy=Node(0)
    #     self.tail=dummy
    #     while l1 and l2:
    #         if l1.value <= l2.value:
    #             tail.next=l1
    #             l1=l1.next
    #         else:
    #             tail.next=l2
    #             l2=l2.next
    #         tail=tail.next
    #     if l1:
    #         tail.next=l1
    #     if l2:
    #         tail.next=l2
    #     return dummy.value
    

    def remove_occurance(self,key):
        if self.head is None:
            return None
        while self.head and self.head.value == key:
            self.head=self.head.next
        temp=self.head
        while temp.next:
            if temp.next.value == key:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return f"{key} not found"
    

    def concat(self,other):
        if self.head is None:
            self.head=other.head
            self.tail=other.head
            self.length=other.length
            return
        if other.head is None:
            return None
        else:
            self.tail.next=other.head
            self.tail=other.tail
        self.length+=other.length

    def frequency(self,value):
        if self.head is None:
            return None
        temp=self.head
        count=0
        while temp:
            if temp.value == value:
                count+=1
            temp=temp.next
        return count
    
    def split_list_value(self,value):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            if temp.value == value:
                temp.next=None
                # break
            temp=temp.next
        return f"{value} is  present"
        

    def traverse(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            while temp:
                print(temp.value,end=" -> ")
                temp=temp.next
            print("none")

l=singlelinkedlist()     
for v in [2,1,90,3,3,3,3,4,5,5,6,7,7]:
    l.append(v)
# l2=singlelinkedlist()
# for v2 in ["x","y","z","w","a","t"]:
#      l2.append(v2)
# l.traverse()
# l.concat(l2)


# l.append(1)
# l.append(1)
# l.append(1)
# l.append(1)
# l.append(2)
# l.append(3)     
# l.append(4)      
# l.append(5) 
l.traverse()  
# l.traverse()
# print(l.get_value(2)) 
l.tail.next=l.head
print("has loop:",l.has_loop())
# print("middle value:",l.middle_value())
print(l.get_nth_node(2))
# print("remove duplicates:",l.remove_duplicate())
# print("remove d:",l.remove_duplicate_sortedlist())
# print("odd,even:",l.odd_even())
# print(l.merge_sorted_lists([1,2,3],[4,5,6]))
# l1 = singlelinkedlist([1, 3, 5])
# l2 = singlelinkedlist([2, 4, 6])

# Create an empty list object just to call methods
# l = singlelinkedlist()

# # Merge heads
# merged_head = l.merge_sorted_lists(l1.head, l2.head)

# # Print result
# l.traverse(merged_head)
# l.remove_occurance(1)
# print(l.sum_linked_list())
# print(l.reverse())
# print("Frequency:",l.frequency(3))
# print("split list by value:",l.split_list_value(5))
# print("remove by value:",l.remove_duplicate_by_value())
l.traverse()  
