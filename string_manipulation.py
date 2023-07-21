#.lstrip()
#str.lstrip() -> strips the white space to left of the string unless characters are given
name = '   Derek    '
print(name) #   Derek    
print(name.lstrip()) #Derek    

a_string = '...hello hi how are you...'
print(a_string) #...hello hi how are you...
print(a_string.lstrip('.h')) #ello hi how are you...

#.rstrip()
#str.rstrip() -> strips the white space to right of the string unless characters are given
print(name) #   Derek    
print(name.rstrip()) #   Derek

print(a_string) #...hello hi how are you...
print(a_string.rstrip('u.')) #...hello hi how are yo

#.strip()
#str.strip() -> strips the white space on both sides of the string unless characters are given

print(name) #   Derek    
print(name.strip()) #Derek

print(a_string) #...hello hi how are you...
print(a_string.strip('.')) #hello hi how are you

#.title()
#str.title() -> returns a version of the string where each word is titlecased

book = 'hArrY PoTTeR aNd ThE goBlEt oF FiRe'
print(book) #hArrY PoTTeR aNd ThE goBlEt oF FiRe
print(book.title()) #Harry Potter And The Goblet Of Fire

#.upper()
#str.upper() -> returns a copy of the string coverted to uppercase

print(book) #hArrY PoTTeR aNd ThE goBlEt oF FiRe
print(book.upper()) #HARRY POTTER AND THE GOBLET OF FIRE

#.lower()
#str.lower() -> returns a copy of the string converted to lowercase

print(book) #hArrY PoTTeR aNd ThE goBlEt oF FiRe
print(book.lower()) #harry potter and the goblet of fire

#.capitalize()
#str.capitalize() -> returns a capitalized version of the string

print(book) ##hArrY PoTTeR aNd ThE goBlEt oF FiRe
print(book.capitalize()) #Harry potter and the goblet of fire