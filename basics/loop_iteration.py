#Break ends the current loop and jumps to the next statement
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done')

#Continue enable current iteration and jump to the top of the loop to start the next iteration
while True:
    line = input('>')
    if line[0]== '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')  


#Definite loop
for i in [5,4,3,2,1]:
    print(i)
print("Blastoff")