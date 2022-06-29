class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        #self.name = name
        #self.phoneNumber = phoneNumber

        #부모클래스의 초기화 메서드를 명시적 호출
        Person.__init__(self,name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    
    #상속받은 메서들르 재정의(덮어쓰기, override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))



p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

#print(p.__dict__)
#print(s.__dict__)

