import random
from statistics import mode

random_digits = [round(random.random()*10) for i in range(15)]
print(random_digits)
print(mode(random_digits))
square_num = [i*i for i in range(2, 4)]
print(square_num)
alpha_num = [f'try{i}' for i in range(3)]
print(alpha_num)
logical_alpha_num = [f'try{i}' for i in range(3) if i%2==0]
print(logical_alpha_num)

alpha = ['abc' for i in range(3)]
print(alpha)

counting = [i for i in range(3)]
print(counting)

odd_num = [i for i in range(10) if i%2!=0]
print(odd_num)
even_num = [i for i in range(6) if i%2==0]
print(even_num)
table_of_two = [f'2 * {i} = {2 * i}' for i in range(6)]
print(table_of_two)


