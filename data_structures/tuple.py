#Tuples are immutable like strings
#they are more efficient, comparable and sortable by a first item

my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple)

#allow duplicates
thistuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple)

print(len(thistuple))
print(type(thistuple))

y = 1,2,3
print(max(y))