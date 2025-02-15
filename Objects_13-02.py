from idlelib.pyshell import usage_msg


class Student:
#     def __init__(self,name,age,id,courses):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.courses = courses
#
#     def __str__(self):
#         return f'{self.courses}<=>{self.id}<=>{self.name}<=>{self.age}'
#
# st1 = Student('zohar',20,314664332,['DevSecOps'])
# st2 = Student('amir',55,7657657655,['DevSecOps','cooking for zero to hero'])
#
# print(st1)
# print(st2)
#


# class Vehicle:
#     def __init__(self, make, model, year: int):
#         self.make = make
#         self.model = model
#         self.year = int(year)
#
#     def __str__(self):
#         return f'{self.make}  {self.model} {self.year}'
#
#     def move(self):
#         print('moving ....')
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, year: int, hp, gear, wheels):
#         super().__init__(make, model, year)
#         self.hp = hp
#         self.gear = gear
#         self.wheels = wheels
#
#
# class Plan(Vehicle):
#     def __init__(self, make, model, year: int, engine_make, seats):
#         super().__init__(make, model, year)
#         self.engine_make = engine_make
#         self.seats = seats
#
#
# class Coupe(Car):
#     def __init__(self, make, model, year: int, hp, gear, wheels, cc):
#         super().__init__(make, model, year, hp, gear, wheels)
#         self.cc = cc
#     1 usage
#     def move(self):
#         print('0 to 100 in 2.9')
#
#
# car1 = Car('mazda', '3', 2023, 200, 5, 4)
# plan1 = Plan('boeing', '787', 2010, 'rolls royce', 300)
# car2 = Coupe('bmw', 'm4 gt4', 2024, 900, 7, 4, 3000)
#
# print(car1)
# print(plan1)
#
# car1.move()
# plan1.move()
# car2.move()
# print(isinstance(car1, Car))
# print(isinstance(car1, Vehicle))
# print(isinstance(plan1, Car))


#
# class Student:
#     def __init__(self,name,age,id,courses):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.courses = courses
#
#     def __str__(self):
#         return f'{self.courses}<=>{self.id}<=>{self.name}<=>{self.age}'
#
# st1 = Student('zohar',20,314664332,['DevSecOps'])
# st2 = Student('amir',55,7657657655,['DevSecOps','cooking for zero to hero'])
#
# print(st1)
# print(st2)
#


class Vehicle:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f'{self.make}  {self.model} {self.year}'

    def move(self):
        print('moving ....')


class Car(Vehicle):
    def __init__(self, make, model, year: int, hp, gear, wheels):
        super().__init__(make, model, year)
        self.hp = hp
        self.gear = gear
        self.wheels = wheels


class Plan(Vehicle):
    def __init__(self, make, model, year: int, engine_make, seats):
        super().__init__(make, model, year)
        self.engine_make = engine_make
        self.seats = seats


class Coupe(Car):
    def __init__(self, make, model, year: int, hp, gear, wheels, cc):
        super().__init__(make, model, year, hp, gear, wheels)
        self.cc = cc


car1 = Car('mazda', '3', 2023, 200, 5, 4)
plan1 = Plan('boeing', '787', 2010, 'rolls royce', 300)
car2 = Coupe('bmw', 'm4 gt4', 2024, 900, 7, 4, 3000)

print(car1)
print(plan1)

car1.move()
plan1.move()
car2.move()
print(isinstance(car1, Car))
print(isinstance(car1, Vehicle))

import time
from abc import abstractclassmethod, ABC


class Server(ABC):
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip
        self.active = False

    @abstractclassmethod
    def start(self):
        pass

    def __str__(self):
        return f'hostname {self.hostname} ip {self.ip} , staus {self.active}'


class WebServer(Server):
    def __init__(self, hostname, ip, port, protocol):
        super().__init__(hostname, ip)
        self.port = port
        self.protocol = protocol

    def start(self):
        self.active = False
        time.sleep(4)
        self.active = True
        print(f'{self.hostname} Rebooted .......')


class DBServer(Server):
    def __init__(self, hostname, ip, db_engin, databases):
        super().__init__(hostname, ip)
        self.db_engin = db_engin
        self.databases = databases

    def start(self):
        print('connecting to the sql server ')


srv1 = Server('web1.server.1', '100.200.230.155')
# srv2 = Server('web1.server.2', '100.52.92.44')
cocopops = WebServer('web2.server.ui', '10.10.5.4', 3000, 'https')
RDS = DBServer('rds1.server.db', '10.55.23.23', 'postgresql', {'users': 3, 'products': 10})

# print(srv1)
print(cocopops)
print(RDS)
# srv1.start()
cocopops.start()

# print(srv1)
print(cocopops)
print(RDS)