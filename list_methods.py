a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list) #['a', 'b', 'c', 'd', 'e']

for letter in a_list:
    print(letter)
#a
#b
#c
#d
#e

print(a_list[0]) #a
print(a_list[4]) #e

a_list[1] = 'B'
print(a_list) #['a', 'B', 'c', 'd', 'e']

#lists can hold any data type
list_of_values = [1, 2, 3, 4.5, 6.7, 'hello', True, False, max, min, len]
print(list_of_values) #[1, 2, 3, 4.5, 6.7, 'hello', True, False, <built-in function max>, <built-in function min>, <built-in function len>]

list_of_lists = [
    ['a', 'b', 'c'],
    [1, 2, 3],
    ['hello', 'hi', 'hey']
]
print(list_of_lists) #[['a', 'b', 'c'], [1, 2, 3], ['hello', 'hi', 'hey']]

print(list_of_lists[0]) #['a', 'b', 'c']
print(list_of_lists[2]) #['hello', 'hi', 'hey']

#.append()
#list.append(value) -> Will add value to the end of the list
print(a_list) #['a', 'B', 'c', 'd', 'e']

a_list.append('f')
print(a_list) #['a', 'B', 'c', 'd', 'e', 'f']

a_list.append('g')
print(a_list) #['a', 'B', 'c', 'd', 'e', 'f', 'g']

#.count()
#list.count(value) -> returns the number of occurences of value

numbers = [1, 1, 1, 2, 3, 4, 5, 7, 7, 4, 3, 3, 4, 6, 7, 8, 5, 3, 3, 5, 7, 4]
num_threes = numbers.count(3)
print(num_threes) #5

#.index()
#list.index(value) -> returns the first index of value
index_of_two = numbers.index(2)
print(index_of_two) #3

print(a_list) #['a', 'B', 'c', 'd', 'e', 'f', 'g']
print(a_list.index('e')) #4

#.insert()
#list.insert(index, value) -> inserts the value at index in list

print(a_list) #['a', 'B', 'c', 'd', 'e', 'f', 'g']
a_list.insert(2, 'z')
print(a_list) #['a', 'B', 'z', 'c', 'd', 'e', 'f', 'g']

#.pop()
#list.pop() or list.pop(index) -> removes and return item at index (defaults to -1)

print(a_list) #['a', 'B', 'c', 'd', 'e', 'f', 'g']
last_element = a_list.pop()

print(a_list) #['a', 'B', 'z', 'c', 'd', 'e', 'f']
print(f"the last element that was removed from the list: {last_element}") #the last element that was removed from the list: g

pop_another = a_list.pop(1)
print(a_list) #['a', 'z', 'c', 'd', 'e', 'f']
print(f"popped: {pop_another}") #popped: B

#.remove()
#list.remove(value) -> removes the first occurence of value

print(a_list) #['a', 'z', 'c', 'd', 'e', 'f']
a_list.remove('c')
print(a_list) #['a', 'z', 'd', 'e', 'f']

#.reverse()
#list.reverse() -> reverses the list *in place* - changes the original list

print(a_list) #['a', 'z', 'd', 'e', 'f']
a_list.reverse()
print(a_list) #['f', 'e', 'd', 'z', 'a']

#.copy()
#list.copy() - copies a list, doesn't alter original
list_a = ['A', 'B', 'C']
list_b = list_a
list_c = list_a.copy()

print(list_a) #['A', 'B', 'C']
print(list_b) #['A', 'B', 'C']
print(list_c) #['A', 'B', 'C']

print(list_a == list_b) #True
print(list_a == list_c) #True
print(list_b == list_c) #True

#.sort()
#list.sort() -> sorts the list in ascending order and returns None. Sorts *in place* 

print(a_list) #['f', 'e', 'd', 'z', 'a']
a_list.sort()
print(a_list) #['a', 'd', 'e', 'f', 'z']

states = ['Illinois', 'Florida', 'California', 'New York', 'Indiana', 'Washington', 'Alabama']
states.sort()
print(states) #['Alabama', 'California', 'Florida', 'Illinois', 'Indiana', 'New York', 'Washington']

states.sort(key=len)
print(states) #['Alabama', 'Florida', 'Indiana', 'Illinois', 'New York', 'California', 'Washington']