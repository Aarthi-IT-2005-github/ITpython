class A:
    def method_A(self):
        print("Method from A")

class B:
    def method_B(self):
        print("Method from B")

class C(A, B):  # Inheriting from A and B
    def method_C(self):
        print("Method from C")

obj = C()
obj.method_A()  # Output: Method from A
obj.method_B()  # Output: Method from B
obj.method_C()  # Output: Method from C
