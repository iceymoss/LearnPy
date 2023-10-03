class BaicInfo:
    # 基本信息
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('(Initialized BaicInfo: {})'.format(self.name))

    def tell(self):
        print(self.name+"今年"+str(self.age)+"性别"+self.gender)

class Teacher(BaicInfo):
    # 老师类
    def __init__(self, name, age, gender, salary):
        BaicInfo.__init__(self, name, age, gender)
        self.salary = salary
        print('(Initialized Teacher: {0})'.format(self.name))

    def tell(self):
        BaicInfo.tell(self)
        print('Salary: "{:d}"\n'.format(self.salary))

class Student(BaicInfo):
    def __init__(self, name, age, gender, marks):
        BaicInfo.__init__(self, name, age, gender)
        self.marks = marks
        print("(Initialized student:{0}".format(self.name))

    def tell(self):
        BaicInfo.tell(self)
        print("marks:'{0}'\n".format(self.marks))
        
    
b = BaicInfo("iceymoss", 22, "male")
# b.tell()

teacher = Teacher("宋浩", 39, "male", 30000)
# teacher.tell()

student = Student("杨旷", 18, "male", 99)
# student.tell()

school = [teacher, student]
for num in school:
    num.tell()

