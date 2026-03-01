class Table:
    def __init__(self, num, start_table, end_table):
        self.num = num
        self.start_table = start_table
        self.end_table = end_table

    total = 0
    even_nums = []
    odd_nums = []

    def table(self):
        for i in range(self.start_table, self.end_table):
            result = f"{self.num} * {i} = {self.num * i}"
            print(result)

    def counting(self):
        for i in range(self.start_table, self.end_table):
            print(i)

    def total_nums(self):
        for i in range(self.start_table, self.end_table):
            self.total += i
        return self.total

    def odd_nums_list(self):
        for i in range(self.start_table, self.end_table):
            if i %2 != 0:
                print(i)

    def even_nums_list(self):
        for i in range(self.start_table, self.end_table):
            if i %2 == 0:
                print(i)

    def list_of_even_nums(self):
        for num in range(0, 11):
            if num %2 == 0:
                self.even_nums.append(num)
        return self.even_nums

    def list_of_odd_nums(self):
        for num in range(0, 11):
            if num %2 != 0:
                self.odd_nums.append(num)
        return self.odd_nums

table12 = Table(12, 1, 11)
table12.table()
table12.counting()
table12.odd_nums_list()
table12.even_nums_list()
print(table12.total_nums())
print(table12.list_of_even_nums())
print(table12.list_of_odd_nums())