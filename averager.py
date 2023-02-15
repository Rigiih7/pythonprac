class student_mean:
    school = 'lvmuthoni'
    def __init__(self, student1, student2, student3):
        self.student1 = student1
        self.student2 = student2
        self.student3 = student3

    def average (self):
        return(self.student1+self.student2+self.student3)/3

    @classmethod
    def getschool(cls):
       return cls.school
    
    @staticmethod
    def mission_statement():
        return('I must make some dollars and marry that b')

form_four = student_mean(90, 50, 70)
form_three = student_mean(80, 60, 48)

print(form_three.average())
print(student_mean.getschool())
print(student_mean.mission_statement())
