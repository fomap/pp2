
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
     
  '''     

list_in = input("Please enter list of numbers ")
list_007 = list_in.split()
str = ''
def has_007(list):
    for i in range(len(list)):
        if list[i] == '0' or list[i] == '7':
            str += list[i]


print(str)






# print(cnt)

# import math

# radius =float(input("Give me the radius"))


# def volume(rad):
#     return  math.pi * (4/3) * rad * rad * rad



# print(volume(radius))




# str1 = input("Please enter string to check for palyndrome ")


# def palindrome(str):
#     str2 = str[::-1]
#     if(str == str2):
#         return True
#     else:
#         return False
        
        
# print(palindrome(str1))


# name = input("Hello! What is your name?")
# adminNumber = randint(1, 20)

# print("Well," +  name + ", I am thinking of a number between 1 and 20.")


# # guestNumber = int(input("Take a  guess"))
# # guessed = False


# # while (guessed == False):
# #     print(guestNumber)

    
# #     elif guestNumber < adminNumber:
# #         print("too low")
# #     elif guestNumber



# string = input("Enter numbers")

# li = list(string.split())
# li2 =  []


# for i in li:
#     li2.append(int(i))
    
# for x in li2:
#     print(x)



# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]



# for i in movies:
#     value1 =  i.get('imdb')
#     print(value1)



# def imdnScore(str):
#     for i in movies:
#         if i.get('name') == str:
#             if i.get('imdb') > 5.5:
#                 return True
#             else:
#                 return False


# inval = input("Enter movie ")
# print(imdnScore(inval))


# subli = []

# def goodMovies():
#     for i in movies:
#         if i.get('imdb') > 5.5:
#             subli.append(i.get('name'))
            
            
            
# goodMovies()
# for i in subli:
#     print(i)


# category = input("Enter the category")

# for i in movies:
#     if i.get("category") == category:
#         print(i.get("name"))










