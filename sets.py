library1 = {'harry_porter', 'davinci_code', 'Angels&Demons', 'richdadpoordad', '50Lawsofpower'}
library2 = {'AtomicHabits', '50Lawsofpower', 'Sadhghuru'}

both = library1.union(library2)
print(both)

common = library1.intersection(library2)
print(common)

diff = library1.difference(library2)
print(diff)

diff2 = library2.difference(library1)
print(diff2)