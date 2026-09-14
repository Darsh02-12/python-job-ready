def two_sum(nums,target):
    seen={}
    compliment=0

    for index, i in enumerate(nums):
        compliment=target-i
        if compliment not in seen:
            seen[i]=index
        else:
            return [seen[compliment],index]

nums=[2, 7, 11, 15]
target=9 

print(two_sum(nums,target))