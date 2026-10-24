def longest_unique(s):
    seen={}
    left=0
    right=0
    max_len=0
    for right in range(len(s)):
        char=s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len=max(max_len,right-left+1)
        right+=1
    return max_len

s="abcabcbb"
print(longest_unique(s))