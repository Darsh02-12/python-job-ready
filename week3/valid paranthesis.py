def is_valid(s):
    par={")":"(","]":"[","}":"{"}
    stack=[]
    top =0
    for char in s:
        if char in "{([":
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                top =stack.pop()
                if top!=par[char]:
                    return False
                
    return len(stack)==0
s="([)]"
print(is_valid(s))