#using open()
#handle = open(filename, mode)
fhand = open('mbox.txt','r')
print(fhand)

#When files are missig
#The newline character \n
staff = 'Hello \n World!'
print(staff)

#The tab character \t
staff1 = 'Hello \t World!'
print(staff1)


#Processing files
#file handle as a sequence
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
    
#Reading the whole line
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#Searchn from a fiel (fixed)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('from'):
        print(line)
        
#or 
for line in fhand:
    if line.startswith('from'):
        print(line)
        
#Skipping with continue
for line in fhand:
    line = line.rstrip()
    if not line.startswith('from'):
        continue
    print(line)