movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

'''
1)
def imdnScore(str):
    for i in movies:
        if i.get('name') == str:
            if i.get('imdb') > 5.5:
                return True
            else:
                return False


inval = input("Enter movie ")
print(imdnScore(inval))

2)
subli = []
def goodMovies():
    for i in movies:
        if i.get('imdb') > 5.5:
            subli.append(i.get('name'))
            
            
goodMovies()
for i in subli:
    print(i)

3)
category = input("Enter the category ")

def printCategory(cat):
    for i in movies:
        if i.get("category") == cat:
            print(i.get("name"))

printCategory(category)

4)
liOfMovies = input("Enter list of movies to calculate average IMDB (list through , with no spaces in between) ")
linew = list(liOfMovies.split(','))

def imdnScore(str):
    for i in movies:
        if i.get('name') == str:
            return i.get('imdb') 
        
def averageOfMovies (list):
    cnt = 0.0
    for x in list:
        temp = imdnScore(x)
        cnt += temp
    
    final = cnt / len(list)
    return final

print(averageOfMovies(linew))
'''

category = input("Enter the category ")

def calCategory(cat):
    result = 0.0
    cnt = 0
    for i in movies:
        if i.get("category") == cat:
            result = result + i.get("imdb")
            cnt = cnt + 1
    final = result / cnt
    return final
print(calCategory(category))
