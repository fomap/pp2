
'''
1)
def convertGrams(num):
    return num * 28.3495231
  
value = float(input("enter ounces "))
print(convertGrams(value))

2)
def convertTemp(num):
    return (num-32) * (5 / 9)
      
value = float(input("enter temp "))
print(convertTemp(value))

3)
def solve(numheads, numlegs):
    chickenlegs = numheads*2 
    rabbitlegs = numlegs-chickenlegs 
    rabbitheads = rabbitlegs/2
    chickenheads = numheads-rabbitheads 
    return chickenheads, rabbitheads

valueheads = int(input("Enter number of heads "))
valuelegs = int(input("Enter number of legs "))
print(solve(valueheads, valuelegs))

4)
def convert(string):
    li = list(string.split(" "))
    return li

def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if(num % i) == 0:
            return False
    return True

value = input("enter list of numbers ")
liInt = []
liPrime = []

for i in convert(value):
    liInt.append(int(i))

def filter_prime(list):
    for i in list:
       if(isPrime(i)):
           liPrime.append(i)
    return liPrime
       
print(filter_prime(liInt))

5)
from itertools import permutations

def allPermutations(str):
	permList = permutations(str)
	for perm in list(permList):
		print (perm)
		
string = input("Enter string ")
allPermutations(string)

6)
sentence = input("Enter sentence please ")

l = sentence.split()
def reverse(list):
    return list[::-1]

for i in reverse(l):
    print(i, end = " ")

7)

list_in = input("Please enter list of numbers ")
list_33 = list_in.split()

def has_33(list):
    for i in range(len(list)):
        if list[i] == '3':
            if i+1 < len(list):
                if list[i+1] == '3':
                    return True
    return False

print(has_33(list_33))            
     

8)

list_in = input("Please enter list of numbers ")
list_007 = list_in.split()
result = []
def has_007(list):
    for i in range(len(list)):
        if list[i] == '0' or list[i] == '7':
            result.append(list[i])

has_007(list_007)
finalstr = ' '.join(result)
if finalstr.find('0 0 7') != -1:
    print(True)
else:
    print(False)


9)
import math
radius =float(input("Give me the radius "))
def volume(rad):
    return  math.pi * (4/3) * rad * rad * rad

print(volume(radius))


   
10)
li = input("Give me a list ")
linew = []
def reinventingSet(list):
    [linew.append(x) for x in li if x not in linew]
    print(linew)

reinventingSet(li)

11)
str1 = input("Please enter string to check for palyndrome ")
def palindrome(str):
    str2 = str[::-1]
    if(str == str2):
        return True
    else:
        return False
            
print(palindrome(str1))

12)
li = input("Please enter histogram ")

def convert(string):
    li = list(string.split(" "))
    return li

liInt = []

for i in convert(li):
    liInt.append(int(i))

def histogram(list):
    for i in list:
        j = 0
        while j < i:
            print('*', end='')
            j+=1
        print("\n")

histogram(liInt)


'''

import random
name = input("Hello! What is your name? ")
print("Well," + name + ", I am thinking of a number between 1 and 20.")
adminNumber = random.randint(1, 20)

guestNumber = int(input("Take a guess "))
guessed = False
cnt = 0


while (guessed == False):
    print(guestNumber)

    if guestNumber == adminNumber:
        guessed = True
        cnt = cnt + 1
        cnt = str(cnt)
        print("Good job, " + name + "! You guessed my number in " + cnt + " guesses!")
        break
    elif guestNumber < adminNumber:
        print("too low ")
        cnt = cnt + 1
    elif guestNumber > adminNumber:
        print("too high ") 
        cnt = cnt + 1
    
    guestNumber = int(input("Take a guess "))









