class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class stack:
    def __init__(self):
        # new_node=Node(value)
        self.top=None
        self.height=0
        self.max_allowed_size=10
    
    def __len__(self):
        return self.height
    
    # def push(self,value):
    #     new_node=Node(value)
    #     if self.height==0:
    #         self.top=new_node
    #     else:
    #         new_node.next=self.top
    #         self.top=new_node
    #     self.height+=1
    #     return value
    def push(self,value):
        if self.max_allowed_size == self.height:
            raise Exception("Stack size limit exceeded")
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        self.height+=1
        return value
    
    def pop(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            self.top.next=self.top
            temp.next=None
        self.height-=1
        return temp
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            None
        # return self.top.value if self.top else None


    def traverse(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            while temp:
                print(temp.value)
                temp=temp.next
l=stack()
print("push is:",l.push(2))
print("push is:",l.push(3))
print("push is:",l.push(4))
print("push is:",l.push(5))
print("push is:",l.push(6))
print("push is:",l.push(7))
print("push is:",l.push(8))
# print("push is",l.push(9))
# print("push is",l.push(10))
# print("push is",l.push(11))
# print("push is",l.push(12))
# print("pop is",l.pop())
print("peek is:",l.peek())
print("len is:",len(l))
l.traverse()