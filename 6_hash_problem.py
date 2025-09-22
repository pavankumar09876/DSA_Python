class Hash:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity
    
    def hash(self,key):
        return hash(key) % self.capacity
    
    def insert(self,key,value):
        index=self.hash(key)
        if self.table[index] is None:
            self.table[index]=[]
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]=(key,value)
        self.table[index].append([key,value])
        return key,value
    
    def get(self,key):
        index=self.hash(key)
        if self.table[index] is None:
            return "nothing"
        for k,v in self.table[index]:
            if k==key:
                return v
        return "Doesn't match"
    
    def find_duplicate(self):
        seen=set()
        duplicate=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for k,_ in bucket:
                if k in seen:
                    duplicate.append(k)
            else:
                seen.add(k) 
        return duplicate,seen

    def key(self):
        keys=[]
        for buckets in self.table:
            if buckets is None:
                continue
            for k,_ in buckets:
                keys.append(k)
        return keys

    def values(self):
        values=[]
        for bucket in self.table:
            if bucket is None:
                continue
            for _,v in bucket:
                values.append(v)
        return values
    
l=Hash(10)
l.insert("pavan",100)
l.insert("pavan1",200)
l.insert("pavan2",300)
# print("get value is:",l.get('pavan2'))
# print("keys is:",l.key())
# print("values:",l.values())
print("find duplicate:",l.find_duplicate())
print(l.table)

def items(l1,l2):
    dict1={}
    for i in l1:
        dict1[i]=True
    for j in l2:
        if j == dict1:
            return True
    return False
i1=[1,2,3]
i2=[4,6,3]
print(items(i1,i2))

def items(l1,l2):
    it=[]
    for i in l1:
        for j in l2:
            if i==j:
                it.append(j)
    return it

l1=[1,2,3]
l2=[4,5,3]
print("items:",items(l1,l2))

def remove_duplicate(arr):
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

arr = [1, 2, 3, 1, 2, 4, 5, 3, 5]
print(remove_duplicate(arr))

def first_non_repeating_char(string):
    char={}
    for ch in string:
        char[ch]=char.get(ch,0)+1
    for ch in string:
        if char[ch] == 1:
            return f"{ch} -> is first non repeating char"
    return None

print(first_non_repeating_char("pavan"))

from collections import Counter
def first_non_repeating_char(string):
    char=Counter(string)
    for ch in string:
        if char[ch]==1:
            return ch
    return None

print(first_non_repeating_char("pavanp"))

def group_anagrams(string):
    anagrams={}
    for word in string:
        key="_".join(sorted(word))
        if key not in anagrams:
            anagrams[key]=[]
        anagrams[key].append(word)
    return list(anagrams.items())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

from collections import defaultdict

def group_anagrams(strings):
    anagrams = defaultdict(list)
    
    for word in strings:
        key = "".join(sorted(word))  
        anagrams[key].append(word)   
    
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


def two_sum_values(arr,target):
    sum1=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                sum1.append((arr[i],arr[j]))
    return sum1,
print(two_sum_values([5, 1, 7, 5, 9, 7, 3], 10))


def two_sum_index(arr,target):
    sum1=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                sum1.append((i,j))
    return sum1,
print(two_sum_index([5, 1, 7, 5, 9, 7, 3], 10))


def has_unique_chars(s):
    char_set=set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True,char_set

 #   return len(s)==len(set(s))
print(has_unique_chars('abcdefg')) 
print(has_unique_chars('pavan')) 
print(has_unique_chars('')) 
print(has_unique_chars('0123456789')) 
print(has_unique_chars('abacadaeaf')) 

# def find_pairs(arr1,arr2,target):
#     pairs=set()
#     for i in range(len(set(arr1))):
#         for j in range(i,len(arr2)):
#             if arr1[i] + arr2[j] == target:
#                 pairs.add((i,j))
#     return pairs


# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# target = 7

# pairs = find_pairs(arr1, arr2, target)
# print (pairs)