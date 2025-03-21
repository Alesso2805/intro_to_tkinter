def add(*args):
    print(sum(args))

add(1, 2, 3, 4, 5,6,7,8,9,10)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=1, multiply=2, divide=3, subtract=4)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R", color="Blue", seats=2)
print(my_car.make)
print(my_car.model)