class avrg_marks:
    school = 'Maserati7'
    def __init__(self, m1, m2, m3):
     self.m1= m1
     self.m2 = m2
     self.m3 = m3

    def average(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def life_motto():
        return('Lavie my love')

s1 = avrg_marks(96, 88, 70)
S2 = avrg_marks(82, 74, 76)

print(s1.average())
print(avrg_marks.life_motto())
print(avrg_marks.getschool())

