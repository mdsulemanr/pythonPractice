def addition(a, b):

    for i in range(0, len(a)):
        if len(a[i])!=len(b):
            return False
    row = []
    ans = []
    i=0
    while i < len(a):
        j=0
        while j < len(b[0]):
            sums = 0
            k=0
            while k < len(b):
                sums = sums + (a[i][k] * b[k][j])
                k+=1
            j+=1
            row.append(sums)
        i+=1
        ans.append(row)
        row = []
    return ans

a=[[1, 2],
   [3, 4]]
b=[[2, 4, 5],
   [3, 2, 0]]

print(addition(a, b))

a=[[1, 2],
   [2, 3],
   [3, 4]]
b=[[2, 4, 5],
   [3, 2, 0]]

print(addition(a, b))


a=[[1, 2, 3],
   [2, 3, 4],
   [3, 4, 1]]

b=[[7, 2, 3],
   [2, 4, 5],
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
