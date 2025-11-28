#Manipulating strings
#strings concatenation
a = 'Hello'
b = a + 'World'
print(b)

#using in as a logical operator 
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)

#strings comparison
word = 'banana'
if word == 'banana':
    print('All right, banana')
    

#String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print("Hi there".lower())
print(greet.upper())

#Search a string
fruit = 'banana'
pos = fruit.find('na')   #finding the first occurrence
print(pos)

aa = fruit.find('z')    #if the string is not found, return -1
print(aa)

#Search and replace
greet = 'hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstx = greet.replace('o', 'x')   #replacing all the o 
print(nstx)

#Strip white space
greet = '    Hello Bob '
strip_ = greet.strip()   #remove all the white space
print(strip_)

left_strip = greet.lstrip()    #remove white space on the left
print(left_strip)

right_strip = greet.rstrip()   #remove white space on the right
print(right_strip)

#Prefix
line = 'Please have a nice day'
yes_ = line.startswith('Please')
print(yes_)

no_ = line.startswith('p')
print(no_)

#Parsing and extraction
data = 'from nkwamzaxolisa@gmail.com Sat Jan 09:14:16 2025'
output = data.find('@')
print(output)

sppos = data.find(' ',output) #will lock for a space after @
print(sppos)

lost = data[output+1:sppos] #slicing (should return gmail.com)
print(lost)