def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")


def default_arguments(table_number=2, limit=10):
    for i in range(limit+1):
        print(table_number, ' * ', i, ' = ', table_number*i)

default_arguments()
default_arguments(3, 5)


def default_arguments(*table_number, limit=11):
    for j in table_number:
        i = 1
        while i < limit:
            print(j, ' * ', i, ' = ', j*i)
            i+=1

default_arguments(2, 3, 4, limit=5)

def test(a, b, c, d=[0]):
    d.append(a)
    d.append(b)
    d.append(c)
    return d

print(test(1, 2, 3))
print(test(1, 2, 3))
print(test(1, 2, 3))