# class Node:                          ----
#     def __init__(self,values,keys):      |
#         self.keys=keys                   |       <----- is not required
#         self.values=values               |
#         self.next=None               ----
# class hash1:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.size=0
#         self.table=[None] * capacity

#     def hash(self,keys):
#         return hash(keys) % self.capacity
    
#     def set_value(self,key,value):
#         index=self.hash(key)
#         if self.table[index] == None:
#             self.table[index]=[]
#         for i,(k,v) in enumerate(self.table[index]):
#             if k==key:
#                 self.table[index][i] = (key,value)
#                 return
#         self.table[index].append((key,value))
#         self.size+=1

#     def get_values(self,keys):
#         index=self.hash(keys)
#         if self.table[index] is None:
#             return f"{keys} key is not present"
#         for k,v in self.table[index]:
#             if k == keys:
#                 return v
#         else:
#             return "Match is not not present"
        
#     def keys(self):
#         all_keys=[]
#         for bucket in self.table:
#             if bucket is None:
#                 continue
#             for k,_ in bucket:
#                 all_keys.append(k)
#         return all_keys

#     def values(self):
#         all_values=[]
#         for bucket in self.table:
#             if bucket is None:
#                 continue
#             for _,v in bucket:
#                 all_values.append(v)
#         return all_values


# l=hash1(10)
# l.set_value("pavan",100)
# l.set_value("aakhil",200)
# l.set_value("aakhil",300)
# print(l.get_values("pavan"))
# print(l.get_values("dp"))
# print(l.keys())
# print(l.values())
# print(l.table)


class hash1:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity
    
    def hash(self,key):
        return hash(key) % self.capacity
    
    def insert(self,key,value):
        index=self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i]=(key,value)
        self.table[index] .append((key,value))
        return key,value
    
    def get(self,key):
        index=self.hash(key)
        if self.table[index] is None:
            return f"{key} key is not found"
        for k,v in self.table[index]:
            if k==key:
                return v
        else:
            return "match not found"
    
    def key(self):
        all_keys=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for k,_ in bucket:
                all_keys.append(k)
        return all_keys

l=hash1(10)
l.insert("pavan",100)
l.insert("pavan1",200)
l.insert("pavan2",300)
print("get value is:",l.get('pavan2'))
print("keys is:",l.key())
print(l.table)
