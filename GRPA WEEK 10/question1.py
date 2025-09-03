GRPA 1 - Calculator Class - GRADED
Problem statement:
Implement a Python class Calculator that stores two numbers and provides methods to perform
addition, subtraction, multiplication, division, and remainder. Division and remainder must
raise ZeroDivisionError when the second operand is zero, following common method/return
conventions in Python exercises [13][14].

Function Specification:
class Calculator(a, b):
    Encapsulates two numeric values and exposes arithmetic methods.

Arguments:
    a: number (first operand)
    b: number (second operand)

Methods:
    add(self) -> number
    subtract(self) -> number
    multiply(self) -> number
    divide(self) -> number  # raise ZeroDivisionError if b == 0
    remainder(self) -> number  # raise ZeroDivisionError if b == 0

Return:
    Each method returns the computed numeric result or raises as specified; signatures and returns
    follow standard function documentation patterns [15][16].

# Solution 

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b  # straightforward return of result [14]

    def multiply(self):
        return self.a * self.b  # standard arithmetic method body [13]

    def subtract(self):
        return self.a - self.b  # consistent naming and return [17]

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")  # explicit guard [13]
        return self.a / self.b

    def remainder(self):
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")  # same contract as divide [13]
        return self.a % self.b
