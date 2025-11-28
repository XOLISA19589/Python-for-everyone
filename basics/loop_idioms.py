#Finding the target value


#counting in a loop
zork = 0
print('Before', zork)

for thing in [9,41,12,3,74,15]:
    zork = zork +1
    print(zork, thing)
print('After', zork)


#summing in a loop
zok = 0
print('before', zok)

for thin in [9,41,12,3,74,15]:
    zok = zok + thin
    print(zok, thin)
print('After', zok)


#finding the range in a loop
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
print(count, sum, value)
print('After', count, sum, sum/count)