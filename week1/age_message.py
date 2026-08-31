def get_age(name,dob):
    age=2026-dob

    if age<13:
        category="child"
    elif age<20:
        category="teenager"
    elif age<60:
        category="adult"
    else:
        category="senior"

    return f"Hi {name}, you will turn {age} this year and you are a {category}" 

name=input("Enter your name: ")
dob=int(input("Enter the year: "))

print(get_age(name,dob))