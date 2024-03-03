'''
1)
def miltiplyList(list):
    res = 1
    for item in list:
        res = res*item
    
    return res


value = input("Enter list of number:")
list = []
for num in value.split():
    list.append(int(num))

print(miltiplyList(list))

2)
def calcLowUpper(string):
    low = upper = 0

    for i in string:
        if i.islower():
            low+=1
        else:
            upper+=1

    return low, upper

value = input("EnTeR sTrInG: ")
lower, upper = calcLowUpper(value)
print("Low = {}, Upper = {}".format(lower, upper))


3)
def palyndrome(string):
    str = string[::-1]
    if str == string:
        return True
    else:
        return False
    
value = input("enter string: ")
print(palyndrome(value))


4)
import math, time
def delay(number, sec):
    time.sleep(sec/1000)
    print("Square root of {} after {} ms is {}".format(number, sec, math.sqrt(number)))

num = int(input("Enter value for sqrt: "))
s = int(input("Enter ms: "))
delay(num, s)


'''

# value = input("Enter tuple values: ")
# list = []

# for item in value.split(" "):
#     # list.append(bool(item))
#     list.append(item)

# tuple = tuple(list)
# print(type(tuple))
# for item in tuple:
#     print(type(item))

def allTrue(t):
    res = all(t)
    return res

tuple = (True, True, True)
print(allTrue(tuple))


tuple = (True, True, False)
print(allTrue(tuple))

