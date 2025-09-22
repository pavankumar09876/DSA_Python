class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,values):
        self.stack.append(values)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "stack is empty1"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def reverse_string(self,string):
        s=Stack()
        reversed_string=""
        for char in string:
            s.push(char)
        while not s.is_empty():
            reversed_string+=s.pop()
        return reversed_string
    
    def sort_stack(self):
        helper=Stack()
        while not self.is_empty():
            temp=self.pop()
            if helper and helper.peek() > temp:
                self.push(helper.pop())
            helper.append(temp)
        self.stack=helper
        while not helper.is_empty():
            self.push(helper.pop())
    
    def is_balanced(self,expresions):
        self.stack=[]
        matching_brackets={')': '(', '}': '{', ']': '['}
        for ch in expresions:
            if ch in '({[':
                self.push(ch)
            elif ch in ')}]':
                if self.is_empty() or self.pop() != matching_brackets[ch]:
                    return False
        return self.is_empty()
    
    def sorted1(self):
        return sorted(self.stack)

s=Stack()
print(s.is_empty())
for i in [34, 3, 31, 98, 92, 23]:
     s.push(i)

# s.sort_stack()
# print(s.stack)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(5)
# s.push(8)
# s.push(90)
# s.push(45)
# s.push(20)
# print("sprt stack:",s.sort_stack())
print("top element:",s.peek())
print("pop:",s.pop())
print("top element:",s.peek())
print("size:",s.size())
print("sorted:",s.sorted1())
# s1="pavan"
# print("reverse string:",s.reverse_string("pavan"))
# print(s.is_balanced("({[]})"))   
# print(s.is_balanced("({[)]}"))   
# print(s.is_balanced("{[()]}"))   
# print(s.is_balanced("{[(])}"))   
# print(s.is_balanced("((()))"))
print(s.is_empty())

class undo_redo:
    def __init__(self):
        self.undo_stack=[]
        self.redo_stack=[]
    
    def do(self,action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("nothing to undo")
            return None

        actions=self.undo_stack.pop()     
        self.redo_stack.append(actions)
        # print(f"undo: {actions}")
        return actions
    
    def redo(self):
        if not self.redo_stack:
            print("nothing to redo")
            return None
        actions=self.redo_stack.pop()
        self.undo_stack.append(actions)
        # print(f"Redo: {actions}")
        return actions
    
    def show_history(self):
        print("Undo stack:", self.undo_stack)
        print("Redo stack:", self.redo_stack)

# editor = undo_redo()

# editor.do("First-youtube")
# editor.do("Second-udemy")
# editor.do("Third-Gemini")

# editor.show_history()

# editor.undo()   # Undo delete
# editor.undo()   # Undo typing "World"
# editor.show_history()

# editor.redo()   # Redo typing "World"
# editor.show_history()

# editor.do("Type '!!!'")  # new action clears redo
# editor.show_history()


# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
    
# class Queue:
#     def __init__(self):
#         self.top=None
#         self.bottom=None
#         self.length=0

#     def enqueue(self,value):
#         new_node=Node(value)
#         if self.top is None:
#             self.top=new_node
#         else:
#             new_node.next=self.top
#             self.top=new_node
#         self.length+=1

#     def view_queue(self):
#         if self.top is None:
#             return None
#         else:
#             temp=self.top
#             while temp:
#                 print(temp.value,end=" -> ")
#                 temp=temp.next
#             print("none")
# l=Queue()
# for i in [1,2,3,4,5,6,7]:
#     l.enqueue(i)

# l.view_queue()


# class undo_redo:
#     def __init__(self):
#         self.undo_stack=[]
#         self.redo_stack=[]
    
#     def do(self,actions):
#         self.undo_stack.append(actions)
#         self.redo_stack.clear()

#     def undo(self):
#         if self.undo_stack is None:
#             return "nothing to undo"
#         actions=self.undo_stack.pop()
#         self.redo_stack.append(actions)
#         return actions
    
#     def redo(self):
#         if self.redo_stack is None:
#             return None
#         actions=self.redo_stack.pop()
#         self.undo_stack.append(actions)
#         return actions
    
#     def show_history(self):
#         print("undo stack:",self.undo_stack)
#         print("redo stack:",self.redo_stack)

# l=undo_redo()
# l.do("youtube")
# l.do("facbook")
# l.do("instagram")
# l.show_history()
# l.undo()
# l.undo()
# l.show_history()
# l.redo()
# l.show_history()
# l.do("chatgpt")
# l.show_history()

