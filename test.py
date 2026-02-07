class Calculator:
    """A simple Python calculator."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b
    
    def modulo(self, a, b):
        """Get remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b


if __name__ == "__main__":
    calc = Calculator()
    
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"17 % 5 = {calc.modulo(17, 5)}")
