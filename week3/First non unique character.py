def first_unique_char(s):
    count={}
    for char in s:
        count[char]=count.get(char, 0) +1
   
    for char in s:
        if count[char]==1:
            return char
    else:
        return None

s="aabbcc"

print(first_unique_char(s))