class Shape:
    def __init__(self, lengthParam):
        self.length = lengthParam

    def getString(self):
        print("Enter value: ")
        invalue = input()
        # print(invalue)
    
    def printString(self):
        print("Enter str")
        str = input()
        str2 = str.upper()
        print(str2)


    


beka = Shape("15")
# lalala = input("enter")
beka.printString()
