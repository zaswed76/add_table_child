

class A:
    def __init__(self):
        self.lst = []

    def lst_app(self, x):
        pass

class B(A):
    def __init__(self):
        super().__init__()

    def lst_app(self, x):
        self.lst.append(x)

b = B()
b.lst_app(3)
print(b.lst)