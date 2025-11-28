#Lists are mutable, meaning their content can be changed, removed, or added
#list within a list [1, [2,3],4]
friends = ['Joseph', 'Glenn', 'Sally']
outfit = [ 'Sock', 'Shirt', 'Jacket']
my_list = []
my_list.append(outfit)
my_list.append(friends)
print(my_list)


lotto = [2,14,26,41,63]
print(lotto[2])

#manipulating list
t = [9,41,12,3,74,15]
print(t[1:3])

#Library: append
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

#check of occurs in a list
some = [1,9,21,10,61]
print(9 in some)
print(15 in some)


#List can be ordered
friends = ['Joeseph', 'Glenn', 'Sally']
friends.sort()
print('I have',len(friends),'friends:',friends)

#List and Strings
abc = 'with three words'
words = abc.split()
print(words)

#Double split
line = 'from Nkwamzaxolisa@gmail.com Fri Nov 28 16:14:30'
words = line.split()
email = words[1]
pieces = email.split('@')
print(words, '\n',email,'\n',pieces)