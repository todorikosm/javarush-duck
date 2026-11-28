class Student:
    all = []

    @classmethod
    def get_avg_mark(cls):
        all_marks = []

        for st in cls.all:
            all_marks.extend(st.marks)

        return sum(all_marks) / len(all_marks)

    def __init__(self, name, age, specialization):
        self.name = name
        self.age = age
        self.specialization = specialization
        self.marks = []
        Student.all.append(self)

    def addMark(self, mark):
        self.marks.append(mark)

    def getAvgMark(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name} {self.specialization} {self.getAvgMark()}"


student_1 = Student("John", 22, "Maths")
student_2 = Student("Piter", 23, "Physics")
student_3 = Student("Garry", 24, "Astronomia")

student_1.addMark(3)
student_1.addMark(4)
student_1.addMark(4)
student_1.addMark(5)

student_2.addMark(5)
student_2.addMark(5)
student_2.addMark(5)
student_2.addMark(5)

student_3.addMark(3)
student_3.addMark(3)
student_3.addMark(4)
student_3.addMark(3)

print(student_1)
print(student_2)
print(student_3)