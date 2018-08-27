def addition(a, b):
    if len(a)!=len(b):
        return False
    for i in range(0, len(a)):
        if len(a[i])!=len(b[i]):
            return False
    c=[]
    i=0
    while i < len(a):
        c.append([])
        j=0
        while j < len(a[i]):
            c[i].append((a[i][j]+b[i][j]))
            j+=1
        i+=1
    return c

a=[[1, 2, 3],
   [2, 3, 4],
   [3, 4, 1]]
b=[[7, 2, 3],
   [2, 4, 5],
   [3, 2, 0]]

print(addition(a, b))

a=[[1, -5],
   [-1, 3],
   [0, 4]]
b=[[7, 2],
   [2, 4],
   [3, 2]]

print(addition(a, b))

a=[[2, 3, 4],
   [3, 4, 1]]
b=[[7, 2, 3],
   [3, 2, 0]]

print(addition(a, b))

a=[[1, 2],
   [2, 3],
   [3, 4]]
b=[[7, 2, 3],
   [2, 4, 5],
   [3, 2, 0]]

print(addition(a, b))

a=[[1, 2, 3],
   [2, 3, 4],
   [3, 4, 1]]
b=[[2, 4, 5],
   [3, 2, 0]]

print(addition(a, b))