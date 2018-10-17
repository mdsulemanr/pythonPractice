a=[10,2,40,-1,'a',10,2,40,100]
dublicate=[]
unique=[]

for i in a:
    if i not in unique:
        unique.append(i)
    dublicate.append(i)

for i in unique:
    print(i, ':', a.count(i))

import collections
print(collections.Counter(a))