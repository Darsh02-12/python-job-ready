# def pair_with_sum(arr,target):
#     for left in range(len(arr)):
#         for right in range(len(arr)-1,left+1):
#             if arr[left]+arr[right]==target:
#                 print(f"target found{arr[left,right]}")
#                 return
#             else:
#                 print("None")
#                 return

# arr=[1, 3, 4, 6, 8, 11]
# target=10
# pair_with_sum(arr,target)

def pair_with_sum(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]+arr[right]==target:
            result=(arr[left],arr[right])
            return result
        elif arr[left]+arr[right]<target:
            left+=1
        else:
            right-=1
    return None

arr=[5,5]
target=10
print(pair_with_sum(arr,target))