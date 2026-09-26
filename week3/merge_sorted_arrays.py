def merge_sorted(list1,list2):
    i=0
    j=0
    new=[]
    while i < len(list1) and j < len(list2):
            if list1[i]<list2[j]:
                new.append(list1[i])
                i+=1
            else:
                new.append(list2[j])
                j+=1
    new.extend(list1[i:]) 
    new.extend(list2[j:])
    return new

list1=[1,2,3]
list2=[10,20,30]

print(merge_sorted(list1,list2))