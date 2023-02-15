#items = {
#    "monitor": lambda X: X*1000,
#      "mouse"   : lambda X: X*1000,
#}
#qauntity = 4
#total_cost = items["monitor"](qauntity)
#print(f"Total cost is {total_cost}")


class marks:
  def __init__(self, m1, m2, m3):
   self.m1=m1
   self.m2=m2
   self.m3=m3

  def avg(self):
    return(self.m1+self.m2+self.m3)/3

s1 = marks(79, 85, 92)
s2 = marks(86, 74, 80)

print(s1.avg())


class marks_avrg:

  school = 'rvg'

  def __init__(self, m1, m2, m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3
  
  def avg(self):
   return (self.m1+self.m2+self.m3)/3
  
  @classmethod
  def getschool(cls):
    return cls.school 
   
  @staticmethod
  def info():
    print("I must ace this game and get em dollars!")

s3 = marks_avrg(77, 75, 90)
s4 = marks_avrg(82, 92, 68)

print(s3.avg())
print(marks_avrg.getschool())
print(marks_avrg.info())
















