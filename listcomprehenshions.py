names = ['Brian', 'Mwirigi', 'Lavinia', 'Muthoni']

print([person for person in names])

l=[]
for name in names:
    l.append(name+ ' together soon')
print(l)

print([name + ' Lovesexdreams' for name in names])

movierating = {'glassonion': 7, 'knivesout': 7, 'womanking': 9, 'Wakanda': 9, 'topgun':5, 'BlackAdam': 5, 'fiftyshades': 2}

print([movie for movie in movierating if movierating[movie]>6])

l = []
for movie in movierating:
  if movierating[movie] < 6:
    l.append(movie)
  print(l)

l = []
for movie in movierating:
 l.append(movie)
print(l)   
