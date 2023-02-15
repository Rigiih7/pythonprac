from collections import Counter
import json
import datetime

store1 = {
        'laptops' : 130,
        'tv_screens' : 100,
        'monitors' : 110
        }

store2 = {
    'laptops' : 450,
    'tv_screens' : 200,
    'monitors' : 240,
    'phones' : 670
    }

combined = Counter(store1) + Counter(store2)

reversed_order = {v*100 : k  for k, v in combined.items()}
print(json.dumps(reversed_order, indent = 4))


person1 = ('Lavie', 24, 'Pizza')
person2 = ('Rigiih', 26, 'lavinia')

couple = (person1, person2)
for name, age,  favfood in couple:
    print(name)
    print(age)
    print(favfood)


class student:
    def __init__(self, name, adm_no):
     self.name = name
     self.adm_no = adm_no

    def display(self):
        print(self.name, self.adm_no)
    
    class baby:
        def __init__(self, jina, gender, birthday):
            self.jina = jina
            self.gender = gender
            self.birthday = birthday

        def show(self):
            print(self.jina, self.gender, self.birthday)
    
    b1 = baby('Rihanna', 'female', '27-6-2026')
    b1.show()


s1 = student('Muthoni', 777)
s2 = student('Mwirigi', 244)
s1.display()
