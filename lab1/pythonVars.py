x = 5
print(x)
print(type(x))
y = "John"
print(y)
print(type(y))
#very unga bunga stuff ngl


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

a = 4
A = "Sally"
print(a)
print(A)


#legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal
'''
2myvar = "John"
my-var = "John"
my var = "John"

'''
print("--------------------")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("--------------------")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("--------------------")
fruits = ["apple", "banana", "cherry"] #unpacking list
x, y, z = fruits
print(x)
print(y)
print(z)

#Output vars
print("--------------------")
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)


#Global vars

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #fantastic

myfunc()

print("Python is " + x) #awesome



x = "awesome"

def myfunc():
  global x #overrides
  x = "fantastic"

myfunc()

print("Python is " + x)


carname = "Volvo"