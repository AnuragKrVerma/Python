# default args
def add2(n1=1,n2=1):
    return n1 +n1

# unlimited arguments
def addunlimited(*arg):
    print(arg[0]) 
    t=0
    for i in arg:
        t += i
    return t

# keyword arguments
def calculator(n , **kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(add2())
print(add2(4,5))

print(addunlimited(2,3,4,4,2,42,68,1,1,1,2,3,89))

print(calculator(0 , add=3,multiply=5))

class Car:
    def __init__(self,**kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan",model = "GT-R",seats=4)
print(my_car.make, ":", my_car.model)
print(my_car.color)
print(my_car.seats)
