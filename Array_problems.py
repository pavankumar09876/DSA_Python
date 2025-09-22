def reverse_swap_list_inplace(arr):
    left=0
    right=len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr

print(reverse_swap_list_inplace([1,2,3,4,5]))


# def max_subarray_sum(nums):
#     if not nums:
#         return 0
#     current_sum=nums[0]
#     max_sum=nums[0]
#     for num in nums[1:]:
#         current_sum=max(num,current_sum+num)
#         max_sum=max(max_sum,current_sum)
#     return max_sum
# print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def intersection_with_duplicates(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i=j=0
    result=[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1
    return result

# arr1 = [1, 2, 2, 1,5]
# arr2 = [2, 2,5,7]
# print(intersection_with_duplicates(arr1,arr2))


def intersection_without_duplicates(arr1,arr2):
    return list(set(arr1)) and set(arr2)

arr1 = [1, 2, 2, 1,5]
arr2 = [2, 2,5]
print(intersection_without_duplicates(arr1,arr2))