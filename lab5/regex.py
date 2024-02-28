import re

'''
1)
def text_gates1(str):
    requirement = '\w*[^a(b*)$]'
    if re.search(requirement, str):
        return ("Its okay")
    else:
        return ("Bad str")


value = input("Enter string:")
print(text_gates1(value))
'''


# def text_gates2(str):
#     requirement = 'ab/{2,3}'
#     if re.search(requirement, str):
#         return ("Yay")
#     else:
#         return ("Nay")
    
# value = input("Enter string:")
# print(text_gates2(value))    redo this part 



# def text_gate3(str):
#     req = "^[a-z]+_[a-z]$"
#     if re.search(req, str):
#         return ("Yay")
#     else:
#         return ("Nay")
    
# value = input("Enter string ")
# print(text_gate3(value))

'''
def txtgate4(str):
    req = '[A-Z]+[a-z]+$'
    if re.search(req, str):
        return ("Yay")
    else:
        return ("Nay")
    

value = input("Enter str: ")
print(txtgate4(value))


def txtgate4(str):
    req = 'a.*?b$'
    if re.search(req, str):
        return ("Yay")
    else:
        return ("Nay")
    

value = input("Enter str: ")
print(txtgate4(value))




def replaceWithColon(str):
    print(re.sub("[ ,.]", ":", str))


value = input("Enter text: ")
replaceWithColon(value)



'''




def snakeToCamel(str):
    print(re.sub("[ ,.]", "", str))

'''
collect  aallwords = capitalize + connect + through kostyl make lower

'''


value = input("Enter text: ")
replaceWithColon(value)




