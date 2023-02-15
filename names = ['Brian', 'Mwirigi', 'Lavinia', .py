names = ['Brian', 'Mwirigi', 'Lavinia', 'Muthoni']
l = []
for name in names:
    l.append(name + ' together soon')
    print(l)

print([name + ' lovesexdreams' for name in names])

movierating = {'glassonion': 7, 'knivesout': 7, 'womanking': 9, 'Wakanda': 9, 'topgun':5, 'BlackAdam': 5, 'fiftyshades': 2}
print([movie for movie in movierating if movierating[movie]>6])

l = []
for movie in movierating:
    if movierating[movie]>7:
        l.append(movie)
        print(l)

lovers = {'Brian', 'Mwirigi', 'Lavinia', 'Muthoni', 'rigiih', 'lavie'}
lover  = {'kamba', 'lavie', 'meru'}
couple = lovers.union(lover)
print(couple)

both = lovers.intersection(lover)
print(both)