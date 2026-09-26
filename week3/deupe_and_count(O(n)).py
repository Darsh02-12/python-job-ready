def dedupe_and_count(number):
    x=[]
    for piece in number.split(","):
        x.append(int(piece))

    y=set()
    simple=[]
    for j in x:
        if j not in y:
            y.add(j)
            simple.append(j)
    

    count={}
    for k in x:
        if k in count:
            count[k]+=1
        else:
            count[k]=1

    return x,list(y),count
number="1,2,3,4,6,5,6,4"

print(dedupe_and_count(number))