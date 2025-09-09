class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class binarysearchtree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        temp=self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else: 
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contains(self,value):
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp=temp.right
            else:
                return temp.value
        return False
                

                    
l=binarysearchtree()

l.insert(47)
l.insert(21)
l.insert(76)
l.insert(18)
l.insert(27)
l.insert(52)
l.insert(82)
print(l.contains(27))
# print(l.contains(100))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         new_node = Node(value)
#         if self.root is None:
#             self.root = new_node
#             return True
#         temp = self.root
#         while True:
#             if value == temp.value:
#                 return False  # no duplicates
#             if value < temp.value:
#                 if temp.left is None:
#                     temp.left = new_node
#                     return True
#                 temp = temp.left
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right

#     def contains(self, value):
#         temp = self.root
#         while temp is not None:
#             if value < temp.value:
#                 temp = temp.left
#             elif value > temp.value:
#                 temp = temp.right
#             else:
#                 return True
#         return False


# # test
# l = BST()
# l.insert(2)
# l.insert(1)
# l.insert(3)
# print(l.contains(2))  # True
# print(l.contains(4))  # False
