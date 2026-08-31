def dedupe_and_count(number):

    numb=[]

    for piece in number.split(","):
        numb.append(int(piece))

    simple=[]

    for num in numb:
        if num not in simple:
            simple.append(num) 

    count={}

    for nums in numb:
        if nums in count:
            count[nums] +=1
        else:
            count[nums] =1

    return numb,simple,count

number=input("Enter the string: ")
print(dedupe_and_count(number))