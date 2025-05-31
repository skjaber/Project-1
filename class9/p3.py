class A:
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def display(self):
        print(f"a1: {self.a1}, a2: {self.a2}, a3: {self.a3}, a4: {self.a4}")

# Class B inherits from class A
class B(A):
    def __init__(self, a1, a2, a3, a4, b1):
        # Calling the __init__ of class A
        super().__init__(a1, a2, a3, a4)
        self.b1 = b1

    def display_b(self):
        # Calling the display method from class A
        self.display()
        print(f"b1: {self.b1}")

# Example usage
b_instance = B(1, 2, 3, 4, 5)
b_instance.display_b()
