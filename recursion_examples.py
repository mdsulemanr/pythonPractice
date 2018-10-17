def zero_count(n):
    if n==[]:
        return 0
    result=0

    if int(n[0])==0:
        result+=1
        result+=zero_count(n[1:])
    result+=zero_count(n[1:])

    return result

n=[1, -1, 6, 9, 5, 0]
print(zero_count(n))
n=[]
print(zero_count(n))

def addition(n):
    n=str(n)
    if n=='':
        return 0
    result = int(n[0]) + addition(n[1:])
    return result

n=123
print(addition(n))
n=0
print(addition(n))
#SAME AS ABOVE
# def addition(n):
#     result=0
#     n=str(n)
#     if n=='':
#         return 0
#     result+=int(n[0])
#     result+=addition(n[1:])
#     return result
#
# n=123
# print(addition(n))
# n=0
# print(addition(n))

def addition(n):
    result = 0
    if n==0:
        return 0
    result+=n
    result+=addition(n-1)
    return result
n=6
print(addition(n))
n=0
print(addition(n))

def factorial(n):
    result=1
    if n==0:
        return 1
    result = result * n
    result*= factorial(n-1)
    return result
n=4
print(factorial(n))
n=0
print(factorial(n))

# def factorial(n):
#     if n==0:
#         return 1
#     result = n * factorial(n-1)
#     return result
#
#
# n=4
# print(factorial(n))
# n=0
# print(factorial(n))

def sumlist(n):
    total=0
    for i in n:
        if not isinstance(i, list):
            total+=i
        else:
            total+=sumlist(i)

    return total

n=[1, 2, [3,4], [5,6]]
print(sumlist(n))