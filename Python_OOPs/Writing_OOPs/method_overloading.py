class MathOperations():
    def add(self,a,b,c=None):
        if c: return a+b+c
        return a+b

int_add = MathOperations()
print(int_add.add(1,2))
print(int_add.add(1,2,3))