def addition(a, b):

    for i in range(0, len(a)):
        if len(a[i])!=len(b):
            return False
    ans=[]
    i=0
    while i < len(a):
        ans.append([])
        j=0
        s=0
        for j in range (0, len(a[i])):
            s+=(a[i][j]*b[j][i])
        ans[i].append(s)
        i+=1

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