from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
class Binarysearchtree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        temp=self.root
        while (True):
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

    # def BFT(self):
    #     current_node=self.root
    #     queus=[]
    #     visited=[]
    #     queus.append(current_node)
    #     while len(queus) > 0:
    #         current_node=queus.pop(0)
    #         visited.append(current_node.value)
    #         if current_node.left is not None:
    #             queus.append(current_node.left)
    #         if current_node.right is not None:
    #             queus.append(current_node.right)
    #     return visited


    # def BFT(self):
    #     # current_node=self.root
    #     queus=[self.root]
    #     visited=[]
    #     # queus.append(current_node)
    #     while len(queus) > 0:
    #         current_node=queus.pop(0)        #dequeue form Front
    #         visited.append(current_node.value)
    #         if current_node.left is not None:
    #             queus.append(current_node.left) # enqueue left child
    #         if current_node.right is not None:
    #             queus.append(current_node.right)   #enqueue right child
    #     return visited

    def BFT(self):
            if self.root is None:
                return []
            queus=deque()
            queus.append(self.root)
            visited=[]
            while len(queus) > 0:
                current_node=queus.popleft()
                visited.append(current_node.value)
                if current_node.left is not None:
                    queus.append(current_node.left)
                if current_node.right is not None:
                    queus.append(current_node.right)
            return visited

    def Depth_First_Search(self):                #Depth First Search Pre_order
        result=[]
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def Depth_first_search_postorder(self):
        visited=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            visited.append(current_node.value)
        traverse(self.root)
        return visited
    
    def Depth_first_search_inorder(self):
        visited=[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            visited.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        return visited
l=Binarysearchtree()
l.insert(47)
l.insert(21)
l.insert(76)
l.insert(18)
l.insert(27)
l.insert(52)
l.insert(82)
print(l.BFT())  
print("Depth_First_Search_pre_order:",l.Depth_First_Search())
print("Depth_First_Search_post_order:",l.Depth_first_search_postorder())
print("Depth_First_Search_in_order:",l.Depth_first_search_inorder())
# print(l.find_min())
# print(l.find_max())        


# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.right=None
#         self.left=None

# class Binarysearchtree:
#     def __init__(self):
#         self.root=None

#     def insert(self,value):
#         new_node=Node(value)
#         if self.root is None:
#             self.root=new_node
#         temp=self.root
#         while True:
#             if new_node.value == temp.value:
#                 return False
#             if new_node.value < temp.value:
#                 if temp.left is  None:
#                     temp.left=new_node
#                     return True
#                 temp=temp.left
#             else:
#                 if temp.right is None:
#                     temp.right=new_node
#                     return True
#                 temp=temp.right
                
#     def Breathfirstsearch(self):
#         current_node=self.root
#         queus=[]
#         visited=[]
#         queus.append(current_node)
#         while len(queus) > 0:
#             current_node=queus.pop(0)
#             visited.append(current_node.value)
#             if current_node.left is not None:
#                 queus.append(current_node.left)
#             if current_node.right is not None:
#                 queus.append(current_node.right)
#         return visited
    
#     def Depth_First_Search_preorder(self):             #(Root -> Left -> Right)
#         result=[]
#         def traverse(current_node):
#             result.append(current_node.value)
#             if current_node.left is not None:
#                 traverse(current_node.left)
#             if current_node.right is not None:
#                 traverse(current_node.right)
#         traverse(self.root)
#         return result
    
#     def Depth_First_Search_postorder(self):      #(Left -> Right -> Root)
#         result=[]

#         def traverse(current_node):
#             if current_node.left is not None:
#                 traverse(current_node.left)
#             if current_node.right is not None:
#                 traverse(current_node.right)
#                 result.append(current_node.value)
#         traverse(self.root)
#         return result
    
#     def Depth_First_Search_inorder(self):        #(Left -> Root -> Right)
#         result=[]
#         def traverse(current_node):
#             if current_node.left is not None:
#                 traverse(current_node.left)
#             result.append(current_node.value)
#             if current_node.right is not None:
#                 traverse(current_node.right)
#         traverse(self.root)
#         return result
    
#     def find_min(self):
#         current = self.root
#         while current.left:
#             current = current.left
#         return current.value

#     def find_max(self):
#         current = self.root
#         while current.right:
#             current = current.right
#         return current.value

# l=Binarysearchtree()
# l.insert(47)
# l.insert(21)
# l.insert(76)
# l.insert(18)
# l.insert(27)
# l.insert(52)
# l.insert(82)
# print("Breath first search:",l.Breathfirstsearch())
# print("Depth_First_Search_pre_order:",l.Depth_First_Search_preorder())
# print("Depth_First_Search_post_order:",l.Depth_First_Search_postorder())
# print("Depth_First_Search_in_order:",l.Depth_First_Search_inorder())
# print(l.find_min())
# print(l.find_max())

# # def Depth_first_search_preorder(self):
# #     visited = []
# #     def traverse(current_node):
# #         if current_node is None:
# #             return
# #         visited.append(current_node.value)      # Root
# #         traverse(current_node.left)             # Left
# #         traverse(current_node.right)            # Right
# #     traverse(self.root)
# #     return visited

# # def Depth_first_search_postorder(self):
# #     visited = []
# #     def traverse(current_node):
# #         if current_node is None:
# #             return
# #         traverse(current_node.left)             # Left
# #         traverse(current_node.right)            # Right
# #         visited.append(current_node.value)      # Root
# #     traverse(self.root)
# #     return visited

# # def Depth_first_search_inorder(self):
# #     visited = []
# #     def traverse(current_node):
# #         if current_node is None:
# #             return
# #         traverse(current_node.left)             # Left
# #         visited.append(current_node.value)      # Root
# #         traverse(current_node.right)            # Right
# #     traverse(self.root)
# #     return visited
