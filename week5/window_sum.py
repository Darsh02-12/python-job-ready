def max_sum(nums,k):
    if k<=0 or k>len(nums):
        raise ValueError(f"k must be in between 1 and {len(nums)}")
    left=0
    window_sum=0
    right=k
    while left<k:
        window_sum+=nums[left]
        left+=1
    maxi_sum=window_sum
    l=right-k   
    while right<=len(nums)-1:
        new_sum=window_sum-nums[l]+nums[right]
        right+=1
        l+=1
        window_sum=new_sum
        if maxi_sum<new_sum:
            maxi_sum=new_sum
    return maxi_sum
        

nums=[2, 1, 5, 1, 3, 2]
k=3
print(max_sum(nums,k))