class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello, {0}".format(self.name))

p = Person("iceymoss")
print(p.say_hi())