import math
'''

1)
def DegreeToRad(n):
#    return math.radians(n)
    result = n/180 * math.pi
    return result


value = float(input("Enter degrees u want to convert "))
print(DegreeToRad(value))


2)
def AreaOfTrapezoid(a, b, h):
    result =  0.5 * (a + b) * h
    return result

sideA = float(input("Enter first value: "))
sideB = float(input("Enter second value: "))
height = float(input("Enter height: "))
print(AreaOfTrapezoid(sideA, sideB, height))


3)
def AreaOfPolygon(num, len): #I^2*n / 4tan180/n where i is length and n is number of sides 
    toppart = len * len * num
    angle = 180/num
    anglerad = math.radians(angle)
    botpart = 4 * math.tan(anglerad)
    result = toppart / botpart
    return result

numberOfSides = float(input("Enter number of sides: "))
lengthOfSide = float(input("Enter length of a side: "))
print(AreaOfPolygon(numberOfSides, lengthOfSide))

'''
def areaOfParallelogram(b, h):
    return b * h

base = float(input("Enter length of base: "))
height = float(input("Enter height: "))
print(areaOfParallelogram(base,height))









