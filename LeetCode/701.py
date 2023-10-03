class Person:
    def say_hi(self):
        print("hi, iceymoss")

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def println_info(self):
        print(self.name+"今年"+str(self.age)+"性别"+self.gender+"\n")
      

p = Person()
p.say_hi()

u = User("iceymoss", 22, "male")
u.println_info()
print(type(u.age))





        