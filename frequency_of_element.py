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

# Alternative (if order doesn’t matter)
# If you don’t care about order, you can just do:

def return_unique(numbers):
    return list(set(numbers))

print(return_unique(a))