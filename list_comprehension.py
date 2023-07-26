#list comprehension
#number comprehension

#with a regular for loop
nums = []
for i in range(1, 101):
    nums.append(i)
print(nums) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#*results* = [*transform* *iteration* *filter*] 

nums_comp = [i for i in range(1, 101)]
print(nums_comp) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

nums == nums_comp #True

#square number comprehension
squared_loop = []

for x in range(1, 11):
    squared_loop.append(x**2)
print(squared_loop) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#list comp
squared_comp = [x**2 for x in range(1, 11)]
print(squared_comp) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#list comprehension with string comprehension
cities = ['Chicago', 'New York', 'Los Angelos', 'Denver', 'Chattanooga']

first_letter = [city[0] for city in cities]
print(first_letter) #['C', 'N', 'L', 'D', 'C']

#adding filters
cities_start_with_c = []

for city in cities:
    if city[0].upper() == 'C':
        cities_start_with_c.append(city)
print(cities_start_with_c) #['Chicago', 'Chattanooga']

#using an 'if' in list comprehension...filter comes after the for

c_cities = [city for city in cities if city[0].upper() == 'C']
print(c_cities) #['Chicago', 'Chattanooga']