#python ternary operator
#value_if_true if condition else value_if_false

num = int(input('Enter a number: '))

if num % 2 == 0:
    name = 'Derek'
else:
    name = 'Fischer'

print(name) #Derek #Fischer -depending on whether the input response was even or odd

numbers = [83, 358, 324, 23, 62, 6092, 58, 3487, 234, 745]

even_or_odd = []

for num in numbers:
    if num % 2 == 0:
        even_or_odd.append('even')
    else:
        even_or_odd.append('odd')
print(even_or_odd) #['odd', 'even', 'even', 'odd', 'even', 'even', 'even', 'odd', 'even', 'odd']

odd_or_even = ['even' if num % 2 == 0 else 'odd' for num in numbers if num < 100]
print(odd_or_even) #['odd', 'odd', 'even', 'even']

x = 15
y = 10
if x > y:
    some_value = 'a'
elif x == y:
    some_value = 'b'
else:
    some_value = 'c'
print(some_value) #a

some_value_again = 'a' if x > y else 'b' if x == y else 'c'
print(some_value_again) #a

#tuples
#defined as an immutable list

#seperated by commas

#lists are mutable - they can be changed
my_list = [1, 2, 3, 4]
my_list[0] = 100
print(my_list) #[100, 2, 3, 4]

#syntax 1: var_tuple = (,)
#syntax 2: var_tuple = , ...,...

tup1 = (1,2,3,4)
print(tup1) #(1, 2, 3, 4)
print(type(tup1)) #<class 'tuple'>

tup2 = 1, 2, 3, 4
print(tup2) #(1, 2, 3, 4)
print(type(tup2)) #<class 'tuple'>

#tuples are indexable
print(tup1[1]) #2
#tuples can be sliced
print(tup1[1:3]) #(2, 3)
#tuples are iterable
for element in tup1:
    print(element)
#1
#2
#3
#4