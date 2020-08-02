class A:
    def __init__(self):
        print("in A")
        super().__init__()

class B(A):
    def __init__(self):
        print("in B")
        super().__init__()


class C(A):
    def __init__(self):
        print("in C")
        super().__init__()

class D(C,B):
    def __init__(self):
        print("in D")
        super().__init__()

d=D()
print(D.mro())
