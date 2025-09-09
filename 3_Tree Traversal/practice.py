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
            return True
        temp=self.root
        while True:
            if value == temp.value:
                return None
            if value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

    def contain_value(self,value):
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp=temp.right
            else:
                return True
        return False
   
    def BFS(self):
        if self.root is None:
            return []
        queue=deque()
        queue.append(self.root)
        visited=[]
        while len(queue) > 0:
            curr_val=queue.popleft()
            visited.append(curr_val.value)
            if curr_val.left is not None:
                queue.append(curr_val.value)
            if curr_val.right is not None:
                queue.append(curr_val.value)
        return visited

    def DFS_pre_Order(self):
        result=[]
        def traverse(current_node):
            if current_node is None:
                return None
            result.append(current_node.value)
            traverse(current_node.left)
            traverse(current_node.right)
        traverse(self.root)
        return result
    
    def DFS_postOrder(self):
        result=[]
        def traverse(current_value):
            if current_value.left is not None:
                traverse(current_value.left)
            if current_value.right is not None:
                traverse(current_value.right)
            result.append(current_value)
        traverse(self.root)
        return result
    
    def DFS_in_Order(self):
        result=[]
        def traverse(current_value):
            if current_value.left is not None:
                traverse(current_value.left)
            result.append(current_value)
            if current_value.right is not None:
                traverse(current_value.right)
        traverse(self.root)
        return result

    def __str__(self):
        return str(self.value)



l=Tree()

l.insert(47)
l.insert(21)
l.insert(76)
l.insert(18)
l.insert(27)
l.insert(52)
l.insert(82)
print(l.contain_value(27))
print(l.contain_value(100))
print("Depth_First_Search_pre_order:",l.DFS_pre_Order())
print("Depth_First_Search_post_order:",l.DFS_postOrder())
print("Depth_First_Search_in_order:",l.DFS_in_Order())
print(l.__repr__())

