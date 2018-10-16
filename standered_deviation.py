import math
def mean(x):
    sum=0
    n=len(x)
    for i in x:
        sum+=i
        average=sum/n

    return average, n

def standard_deviation(x):
    average, n = mean(x)
    summation=0
    for i in x:
        summation+=(i-average)**2
    SD=math.sqrt(summation/(n-1))
    return SD

x=[12, 15, 17, 20, 30, 31, 43, 44, 54]
print(standard_deviation(x))

def standard_deviation_grouped(x, f):
    average, n = mean(x)
    summation=0
    summation_f=sum(f)

    for i, j in zip(x, f):
        summation+=j*(i-average)**2
    SD=math.sqrt(summation/summation_f)
    return SD

x=[4, 5, 6, 7, 8]
f=[9, 14, 22, 11, 17]

print(standard_deviation_grouped(x, f))

