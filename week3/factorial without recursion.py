def factorial(n):

    result=1

    for i in range (1,n+1):
        result=result*i

    return result

n=5

def fibonacci(n):
    a=0
    b=1
    for i in range (1,n):
        a,b=b,a+b
    return b

print(factorial(n))

n=6
print(fibonacci(n))