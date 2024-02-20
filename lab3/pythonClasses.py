'''
1)
class FirstTask():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter any string ")

    def printString(self):
        print(self.string)


example = FirstTask()
example.getString()
example.printString()

class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, lengthParam):
        self.length = lengthParam

    def area(self):
        return self.length * self.length


shape1 = Shape()
print(shape1.area())

shape2 = Square(10)
print(shape2.area())

3)
class Rectangle(Shape):
    def __init__(self, lengthParam, widthParam):
        self.length = lengthParam
        self.width = widthParam
    
    def area(self):
        return self.length * self.width

shape3 = Rectangle(2, 3)
print(shape3.area())


4)
class Point:
    def __init__(self, xParam, yParam, zParam):
        self.x = xParam
        self.y = yParam
        self.z = zParam

    def show(self):
        print("X is {}, Y is {}, Z is {}".format(self.x, self.y, self.z))

    def move(self, newX, newY, newZ):
        self.x = newX
        self.y = newY
        self.z = newZ
    
    def dist(self, newPoint):
        a = self.x - newPoint.x
        b = self.y - newPoint.y
        c = self.z - newPoint.z
        print("Distance is {}, {}, {}".format(a, b, c))

pnt1 = Point(145, 10, 85)
pnt1.show()
pnt1.move(0,0,0)
pnt1.show()
pnt2 = Point(14, 5, 6)
pnt1.dist(pnt2)

5)
class Account:
    def __init__(self, ownerParam, balanceParam):
        self.owner = ownerParam
        self.balance = balanceParam

    def deposit(self, depositMoney):
        self.balance += depositMoney
        print("successfully deposited {} KZT, currrent balance {}".format(depositMoney, self.balance))

    def withdraw(self, withdrawMoney):
        if withdrawMoney > self.balance:
            print("Operation avalilable, not enough money")
        else:
            self.balance -= withdrawMoney
            print("successfully withdrawn {} KZT, currrent balance {}".format(withdrawMoney, self.balance))


test1 = Account("Beka", 100)
test1.deposit(150)      
test1.withdraw(1000)
'''

def prime(num):
    if num == 0 or num == 1:
        return False
    

    for i in range(2, num):
        if(num%i == 0):
            return False
        
    return True


li = [3,345,6,15,1,5,6,2,0,7,95,4,7]

primes = list(filter(lambda x: prime(x), li))
print(primes)



