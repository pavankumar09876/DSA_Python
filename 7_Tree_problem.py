from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return None
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
            elif value > temp.right:
                temp=temp.right
            return True
        return False

    def BFS(self):
        if self.root is None:
            return []
        queue=deque() 
        queue.append(self.root)
        visited=[]
        while len (queue) > 0:
            current_node=queue.popleft()
            visited.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return visited
        
    def DFS_Preorder(self):
        result=[]
        def traversal(current_node):
            if current_node is None:
                return 
            result.append(current_node.value)
            # if current_node.left is not None:
            traversal(current_node.left)
            # if current_node.right is not None:
            traversal(current_node.right)
        traversal(self.root)
        return result


    def DFS_Postorder(self):
        visited=[]
        def traversal(current_node):
            # if current_node.left is not None:
            if current_node is None:
                return 
            traversal(current_node.left)
            # if current_node.right is not None:
            traversal(current_node.right)
            visited.append(current_node.value)
        traversal(self.root)
        return visited

    def DFS_Inorder(self,node,res=None):
        if res is None:
            res=[]
        if node:
            self.DFS_Inorder(node.left,res)
            res.append(node.value)
            self.DFS_Inorder(node.right,res)
        return res

    # def DFS_Inorder(self):
    #     visited=[]
    #     def traversal(current_node):
    #         if current_node is None:
    #             return 
    #         # if current_node.left is not None:
    #         traversal(current_node.left)
    #         visited.append(current_node.value)
    #         # if current_node.right is not None:
    #         traversal(current_node.right)
    #     traversal(self.root)
    #     return visited
    
    def min(self):
        current=self.root
        while current.left:
            current=current.left
        return current.value

    def max(self):
        current=self.root
        while current.right:
            current=current.right
        return current.value
    
    # def k_smallest_element(self,k):
    #     result=[]
    #     def inorder(node):
    #         if not node or len(result) >= k:
    #             return
    #         inorder(node.left)
    #         result.append(node.value)
    #         inorder(node.right)
    #     inorder(self.root)
    #     return result[k-1] if len(result) >=k else None

    def kth_smallest_node(self, k):
        list = self.DFS_Inorder(l.root)
        if k < 0 or k > len(list):
            return "index out or range"  
        return f"The node value at position '{k}' in BST from sorted order is '{list[k-1]}'"
    
    def is_valid_bst(self):
        node_values = self.DFS_Inorder()
        for i in range(1, len(node_values)):
            if node_values[i] <= node_values[i-1]:
                return False
        return True

l=Tree()
l.insert(47)
l.insert(21)
l.insert(76)
l.insert(18)
l.insert(27)
l.insert(52)
l.insert(82)
# print(l.contains(18))
# print(l.BFS())
# print("DFS_Preorder",l.DFS_Preorder())
# print("DFS_Postrder",l.DFS_Postorder())
print("DFS_Inorder",l.DFS_Inorder(l.root))
# print(l.min())
# print(l.max())
print(l.kth_smallest_node(4))
# print(l.is_valid_bst())

