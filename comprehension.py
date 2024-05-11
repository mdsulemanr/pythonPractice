my_dict = {i:i+7 for i in range(1, 10)}
print(my_dict)


# tupple comprehension
(i for i in (1, 2, 3))

# list comprehension
my_list = [i for i in range(1, 10)]

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass
