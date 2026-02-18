for num in range(0, 101):
    if num %2 != 0:
        print(num)

for num in range(0, 101):
    if num %2 == 0:
        print(num)

for num in range(0, 101):
    if num %3 == 0 and num %10 == 0:
        print(num)

for num in range(0, 101):
    if num %2 == 0 or num %7 == 0:
        print(num)

start_table = 1
end_table = 1235
for i in range(start_table, end_table):
    print(f"1234 * {i} = {1234*i}")