#Dictionary is a linear collection og key-value pairsand it is mutable
cabinet = dict()
cabinet['Summer']= 12
cabinet['Fall'] = 3
cabinet['spring'] = 75
print(cabinet)

print(cabinet['Fall'])

#Dictionaries and files
data = {'chick': 1, 'fred': 42, 'jan': 100}
print(data)
print(list(data))
print(list(data.keys()))
print(list(data.values()))
print(list(data.items()))