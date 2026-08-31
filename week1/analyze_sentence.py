def analyze_sentance(s):
    

    length=(len(s.split()))
    revers=s[::-1]

    for char in s:
        if char.lower() in {"a","e","i","o","u"}:
            s=s.replace(char,"")

    return length,revers,s

s=input("enter the sentence: ")
print(analyze_sentance(s))