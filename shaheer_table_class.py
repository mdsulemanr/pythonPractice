# 2 * 1 = 2
# 2 * 2 = 4

class Table:
    def __init__(self, num, start_table, end_table):
        self.num = num
        self.start_table = start_table
        self.end_table = end_table

    def table(self):
        for i in range(self.start_table, self.end_table):
            result = f"{self.num} * {i} = {self.num * i}"
            print(result)

    def counting(self):
        for i in range(self.start_table, self.end_table):
            print(i)

    def total_nums(self):
        total = 0
        for i in range(self.start_table, self.end_table):
            total += i
        return total

    def odd_nums(self):
        for i in range(self.start_table, self.end_table):
            if i %2 != 0:
                print(i)

    def even_nums(self):
        for i in range(self.start_table, self.end_table):
            if i %2 == 0:
                print(i)

    def list_of_even_nums(self):
        appends_name = []
        for num in range(0, 11):
            if num %2 == 0:
                appends_name.append(num)
        return appends_name

    def list_of_odd_nums(self):
        appends_name2 = []
        for num in range(0, 11):
            if num %2 != 0:
                appends_name2.append(num)
        return appends_name2

table12 = Table(12, 1, 11)
table12.table()
table12.counting()
table12.odd_nums()
table12.even_nums()
print(table12.total_nums())
print(table12.list_of_even_nums())
print(table12.list_of_odd_nums())