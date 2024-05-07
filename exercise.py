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

#Create a list of numbers that are les than ten using l_1 and list comprehension

#Your output should = [1, 5, 8, 9]

#use the following list - [1, 11, 14, 5, 8, 9]

l_1 = [1, 11, 14, 5, 8, 9]

l_comp = [num for num in l_1 if num < 11]
print(l_comp) #[1, 5, 8, 9]

#Using list comprehension, create a list of names of 4 letters or more and capitalize each name
names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
names3 = [names.capitalize() for names in names1 if len(names) >= 4]
print(names3) #['Connor', 'Connor', 'Connor', 'Evan', 'Evan', 'Kevin']

#bonus challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
names4 = [name.capitalize() for name in names2 if isinstance(name, str) and len(name) >= 4]
print(names4) #['Connor', 'Connor', 'Connor', 'Evan', 'Evan', 'Kevin']