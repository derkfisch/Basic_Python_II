#strip all white space and capitalize every name in list given

names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
#output: ['Connor', 'Max', 'Evan', 'Jordan']

print(names) #['    coNNor', 'max', ' EVan ', 'JORDAN']

new_names = []
for name in names:
    new_names.append(name.strip().title())

print(new_names) #['Connor', 'Max', 'Evan', 'Jordan']

#remove all duplicates

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

nondupes = []

for name in names:
    while name not in nondupes:
        nondupes.append(name)

print(nondupes) #['connor', 'bob', 'evan', 'max', 2, 3, 4, 'kevin']