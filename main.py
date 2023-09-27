class Person:
    name = 'Nurbek'
    age = 16
    city = 'Bishkek'

    def say(self):
        return 'hello'


a = Person()
print(a.say())


class Car:
    name = 'Mercedes'
    model = 'GLE-coupe'
    capacity = 3.5
    color = 'White'
    wheels = 'x4 + 1'

    def sostoyanie(self):
        return 'very good!'


a = Car()
print(a.sostoyanie())


class car:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


a = car('Mercedes, GlE-Coupe', 3.5)
print(a.name, a.capacity)


class plus:

    def __init__(self, first, second):
        self.first = first
        self.second = second


a = plus(50, 100)
print(a.first + a.second)


class school:
    def __init__(self):
        pass