class Calculator:
    def __init__(self, num1, num2):
        print(f" {" .*.<=>.*. " * 5} {"Simple Calculator".upper()} {" .*.<=>.*. " * 5} ")
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        result = self.num1 + self.num2
        return result

    def subtraction(self):
        result = self.num1 - self.num2
        return result

    def multiplication(self):
        result = self.num1 * self.num2
        return result

    def division(self):
        result = self.num1 / self.num2
        return result

    def remainder(self):
        result = self.num1 % self.num2
        return result

calculator = Calculator(1, 5)
print(calculator.addition())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())
print(calculator.remainder())