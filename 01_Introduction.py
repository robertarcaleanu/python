# Concatenate variables
num = 12
name = 'Rob'

print('My number is {} and my name is {}'.format(num, name))

# Select character from a string
print(name[0])
print(name[1:3])
print(name[1:])

# Lists
my_list = ['a', 'b', 'c']
print(my_list[0])
my_list.append('d')
print(my_list[2:])

# dictionary

d = {'key1': 'value', 'key2': 123}
print(d['key1'])

d1 = {'k1':{'innerKey':[1, 2, 3]}}
print(d1['k1']['innerKey'])

# Tuple
t = (0, 1, 2) # we can't reasign value
print(t)
print(t[0])

s = {1, 2, 3}
s.add(5)
print(s)

# Conditionals

if 1 == 2:
    print('one')
elif 3 == 3: 
    print('middle')
else:
    print('last')

# Loop
seq = [1, 2, 3, 4]

for i in seq:
    print(i)

out = []

for i in range(10):
    out.append(i**2)

print(out)

print([i**2 for i in range(10)])

# Functions
def my_func(myParam):
    print(myParam)

my_func('This is a function!')

# Map

def times2 (var):
    return var**2

seq = range(10)
print('result obtained with map')
print(list(map(times2, seq)))
print(list(map(lambda num: num**2, seq))) # we can also use lambda

# filter 

print(list(filter(lambda num: num%2 == 0, seq)))

# methods
s = 'My name is Robert'
print(s.lower())
print(s.upper())
print(s.split())

# in operator
print('x' in [1, 2, 3])

