import re

'''

def text_gates1(str):
    requirement = '^a(b*)$'
    if re.search(requirement, str):
        return ("Its okay")
    else:
        return ("Bad str")


value = input("Enter string:")
print(text_gates1(value))



def text_gates2(str):
    requirement = 'ab{2,3}'
    if re.search(requirement, str):
        return ("Yay")
    else:
        return ("Nay")
    
value = input("Enter string:")
print(text_gates2(value))  



def text_gate3(str):
    req = '^[a-z]+_[a-z]+$'
    if re.search(req, str):
        return ("Yay")
    else:
        return ("Nay")
    
value = input("Enter string ")
print(text_gate3(value))





def txtgate4(str):
    req = '[A-Z]+[a-z]+$'
    if re.search(req, str):
        return ("Yay")
    else:
        return ("Nay")
    

value = input("Enter str: ")
print(txtgate4(value))




def txtgate5(str):
    req = 'a.*?b$'
    if re.search(req, str):
        return ("Yay")
    else:
        return ("Nay")
    

value = input("Enter str: ")
print(txtgate5(value))




def replaceWithColon(str):
    print(re.sub("[ ,.]", ":", str))

value = input("Enter text: ")
replaceWithColon(value)





def convToUpperCase(str):
    print(re.findall('[A-Z][^A-Z]*', str))

value = input("Enter text: ")
convToUpperCase(value)



def insertSpaceBetweenWords(str):
    print(re.sub(r"(\w)([A-Z])", r"\1 \2", str))

value = input("Enter text: ")
insertSpaceBetweenWords(value)




def snakeToCamel(str):
   
    str = re.sub("[_]", " ", str)

    newstr = str.title()
    newstr = re.sub(" ", "", newstr)
    res = newstr[0].lower() + newstr[1:]
    return(res)


value = input("Enter text: ")
print(snakeToCamel(value))
'''



def camelToSnake(str):
    newstr = re.sub(r"([A-Z])",  r" \1", str)
    newnewstr = newstr.lower()
    res = re.sub(r" ",  r"_", newnewstr)
    out = res[1:] #lowkey situational(?)
    return(out)

value = input("Enter text: ")
print(camelToSnake(value))



