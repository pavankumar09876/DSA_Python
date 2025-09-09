# def my_list(list1,list2):
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 return True
#     return False
# list1=(1,2,3)
# list2=(4,5,3)
# print(my_list(list1,list2))


# def my_list(list1,list2):
#     my_dict={}
#     for i in list1:
#         my_dict[i]=True
#     for j in list2:
#         if j in my_dict:
#             return True
#     return False
# list1=(1,2,3)
# list2=(4,5,3)
# print(my_list(list1,list2))


class Hash:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity

    def hash1(self,key):
        return hash(key) % self.capacity
    
    def set_value(self,key,value):
        index=self.hash1(key)
        if self.table[index] is None:
            self.table[index] =[]
        for i ,(k,v) in enumerate(self.table[index]):
            if k==key :
                self.table[index][i] =(key,value)
        self.table[index].append((key,value))
        self.size+=1

    def get_value(self,key):
        index=self.hash1(key)
        if self.table[index] is None:
            return None
        for k,v in self.table[index]:
            if k==key:
                return v
        else:
            return None
        
    def keys(self):
        all_keys=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for k,_ in bucket:
                all_keys.append(k)
        return all_keys
    
    def values(self):
        all_keys=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for _,v in bucket:
                all_keys.append(v)
        return all_keys


l=Hash(10)
l.set_value("pavan",400)
l.set_value("aakhil",500)
l.set_value("pavan",600)
print()
print(l.table)
print(l.get_value("pavan"))
print(l.get_value("shabbir"))
print(l.keys())
print(l.values())    
