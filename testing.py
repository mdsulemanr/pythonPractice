def get_num(message1, message2):
    while True:
        try:
            num = int(input(message1))
            break
        except ValueError:
            print(message2)
    return num

message1 = "Please enter a number: "
message2 = "Invalid input! Enter whole numbers only!"

list_of_num = []

for i in range(0, 6):
    abc = get_num( message1, message2 )
    list_of_num.append(abc)

print(list_of_num)