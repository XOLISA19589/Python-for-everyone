#INDEXING
fruit = 'banana'
letter = fruit[1]
print(letter) #since index start from 0, this will print a.

x = 3
w = fruit[x-1] #this will print n (first n from banana)
print(w)

print(len(fruit))

#Slicing
s = 'Monty Python'
print(s[0:4]) #it will start from 0 but wont print the letter at 4. (Mont)
print(s[6:7]) #it will print number at 6. (P)
print(s[6:20])   #it will start from 6 but wont print the letter at 20. (Python)

print(s[:2]) #will print the first letters. (Mo)
print(s[8:]) #will pring from letter8 and the rest. (thon)
print(s[:]) #will return s