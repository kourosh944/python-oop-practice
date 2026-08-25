class A:
    def __init__(self):
        print("A-1")

class B(A):
    def __init__(self):
        print("B-1")
        super().__init__()
        print("B-2")

obj = B()
