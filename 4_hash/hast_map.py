# class Node:
#     def __init__(self,key,value):
#         self.key=key
#         self.value=value
#         self.next=None
# class hash1:
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.size=0
#         self.table=[None] * capacity

#     def hash(self,key):
#         return hash(key) % self.capacity
    
#     def set_value(self,key,value):
#         index=self.hash(key)
#         if self.table[index]== None:
#             self.table[index]=[]
#             # for i, (k,v) in enumerate(self.table[index]):
#             #     if k==key:
#             #         self.table[index][i] = (key,value)
#             #         return
            
#         self.table[index].append((key,value))

# l=hash1(7)
# l.set_value("pavan:",400)
# l.set_value("aakhil:",500)
# # l.set_value("pavan:",600)
# print(l.table)


class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Hash1:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity
    
    def hash(self,key):
        return hash(key) % self.capacity

    def set_value(self,key,value):
        index=self.hash(key)
        if self.table[index] == None:
            self.table[index]= []
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key,value)
                return
        self.table[index].append((key,value))
        self.size+=1

    def get_value(self,key):
        index=self.hash(key)
        if self.table[index] is None:
            return f"{key} key is not present"
        for k,v in self.table[index]:
            if k==key:
                return v
        else:
            return "match not found"

    def keys(self):
        all_keys=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for k,_ in bucket:
                all_keys.append(k)
        return all_keys

    def values(self):
        all_values=[]
        for buckets in self.table:
            if buckets is None:
                continue
            for _,v in buckets:
                all_values.append(v)
        return all_values
l=Hash1(10)
l.set_value("pavan",400)
l.set_value("aakhil",500)
l.set_value("pavan",600)
print()
print(l.table)
print(l.get_value("pavan"))
print(l.get_value("shabbir"))
print(l.keys())
print(l.values())
