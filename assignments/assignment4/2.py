class Student: #{
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #determine grade
    def grade(self):
        if self.score >= 85:
            return "HD"
        elif self.score >= 75:
            return "D"
        elif self.score >= 65:
            return "C"
        elif self.score >= 50:
            return "P"
        else:
            return "F"
#}

#main program
#get number of students
student_number = int(input("Enter number of students: "))
for i in range(student_number):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    student = Student(name, int(score))
    grade = student.grade()
    #print out
    print("{} - {} - ({})".format(name,score,grade))