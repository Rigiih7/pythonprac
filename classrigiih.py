class rigiih:
    newlife = 'Rich this year on God'
    def __init__(self, money1, money2, money3):
        self.money1 = money1
        self.money2 = money2
        self.money3 = money3

    def average(self):
        return(self.money1+self.money2+self.money3)/3
    
    @classmethod
    def getnewlife(cls):
        return cls.newlife
    
    @staticmethod
    def humble_prayer():
        return('God grant me your favour. May I get money, health and more money this year. Amen. ')

m1 = rigiih(1000000, 997990, 777667)
m2 = rigiih(23930000,10234567, 14740678)

print(m1.average())
print(m2.average())
print(rigiih.getnewlife())
print(rigiih.humble_prayer())