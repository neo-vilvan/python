class Calculating:
    def add(self, a,b):
        return a + b
    
    def sub(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

o1 = Calculating()
print(o1.add(5,10))
print(o1.sub(5,10))
print(o1.product(5,10))
print(o1.divide(5,10))
    
class PythonProg:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def newfunc(self):
        print("Hi, my name is "+ self.name + " and my age is "+ self.age) 

p1 = PythonProg("Python", "31")
p1.newfunc()