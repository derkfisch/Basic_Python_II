#input()

answer = input('What is the answer to this input?')

print(answer) #whatever you end up typing for the input will be repeated back at you as the answer
print(type(answer)) #<class 'str'> #input aLways returns a string

#isinstance()
#isinstance(obj, class) -> returns True if object is an instance class, False otherwise

print(isinstance(10, int)) #True
print(isinstance('hello', str)) #True
print(isinstance('hello', float)) #False

#len()
#len(obj) -> return the number of items in the object

random_list = [324, 354, 46, 13, 1324, 46, 5, 25, 3, 45, 567, 134]
length = len(random_list)
print(length) #12

random_string = 'rjdksfhn'
length_of_string = len(random_string)
print(length_of_string) #8

#max()
#max(iterable) -> returns the largest value in the iterable

print(random_list) #[324, 354, 46, 13, 1324, 46, 5, 25, 3, 45, 567, 134]

largest_element = max(random_list)
print(largest_element) #1324

some_string = 'azure'
print(max(some_string)) #z

#min()
#min(iterable) -> returns the smallest value in the iterable

print(random_list) #[324, 354, 46, 13, 1324, 46, 5, 25, 3, 45, 567, 134]

smallest_element = min(random_list)
print(smallest_element) #3

some_string = 'azure'
print(min(some_string)) #a

#range()
#range(stop) -> if only one argument, defaults to 0, goes up to but not including stop
#range(start, stop) -> if two args, first argument is start (inclusive), second is stop (exclusive)
#range(start, stop, step) -> third argument is the step (increment or decrement)

for i in range(10):
    print(i)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

for x in range(10, 20):
    print(x)
#10
#11
#12
#13
#14
#15
#16
#17
#18
#19

for t in range(10, 50, 5):
    print(t)
#10
#15
#20
#25
#30
#35
#40
#45

#round()
#round(val, precision) -> return the value rounded to precision
#if precision > 0, round to that many decimal places to the right of the decimal
#if precision < 0, round to that many decimal places to the left of the decimal e.g. -1 rounds to the 10s, -2 rounds to the 100s, ect

unrounded_value = 10.342423
rounded = round(unrounded_value, 0)
print(rounded) # 10.0

#sum()

nums = [23, 34, 57, 234, 57, 234, 872, 46]
total = sum(nums)

print(total) #1557