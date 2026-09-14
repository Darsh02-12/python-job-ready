def is_anagram(s1,s2):

    s1=sorted(s1.lower())
    s2=sorted(s2.lower())

    if s1 ==  s2:
        return True
    else:
        return False


s1="rat"
s2="car"

print(is_anagram(s1,s2))