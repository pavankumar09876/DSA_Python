from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
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

    def BreathFirstSearch(self):
        if not self.root:
            return []
        queue=deque()
        queue.append(self.root)
        visited=[]
        while queue:
            current_node=queue.popleft()
            visited.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return visited
    
    def Depth_first_search_preorder(self):
        visited=[]
        def traverse(current_node):
            visited.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return visited
    
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
    
l=binarysearchtree()
l.insert(47)
l.insert(21)
l.insert(76)
l.insert(18)
l.insert(27)
l.insert(52)
l.insert(82)
print("Breath first search:",l.BreathFirstSearch())
print("Depth_First_Search_pre_order:",l.Depth_first_search_preorder())
print("Depth_First_Search_post_order:",l.Depth_first_search_postorder())
print("Depth_First_Search_in_order:",l.Depth_first_search_inorder())




