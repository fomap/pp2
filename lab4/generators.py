
'''
1)
def Squares(n):
    i = 1
    while i <= n:
        result = i * i
        yield result
        i = i + 1

value = int(input("Enter number "))
for result in Squares(value):
    print (result)


2)
def EvenPrinter(n):
    for i in range (0, n, 2):
        yield i

value = int(input("Enter number"))
for i in EvenPrinter(value):
    print(i, end=",")



3)
def ThreeFourDivider(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

value = int(input("Enter number"))
for i in ThreeFourDivider(value):
    print(i)


4)
def AtoBSquares(a, b):
    for i in range(a, b):
        yield i * i

floor = int(input("Enter start "))
ceiling = int(input("Enter finish "))


for i in AtoBSquares(floor, ceiling):
    print(i)
'''


def Reverse(n):
    i = n
    while i >= 0:
        yield i
        i = i - 1


value = int(input("enter number"))
for i in Reverse(value):
    print(i)






