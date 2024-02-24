'''
import datetime


1)
def backToPast(n):
    return datetime.date.today() - datetime.timedelta(n)

value = int(input("enter how far to go back"))
print(backToPast(value))



2)
def threeDays():
    yesterday = datetime.date.today() - datetime.timedelta(1)
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(1)
    return yesterday, today, tomorrow

print(threeDays())

3)

def dropMilliseconds():
    rightNow = datetime.datetime.now()
    formatted = rightNow.strftime("%m/%d/%Y, %H:%M:%S")
    return formatted

print(dropMilliseconds())
'''


from datetime import datetime


def diffFunction(str1, str2):
    day1_object = datetime.strptime(str1, '%Y-%m-%d %H:%M:%S')
    day2_object = datetime.strptime(str2, '%Y-%m-%d %H:%M:%S')
    diff = day1_object - day2_object
    return diff.total_seconds()


day1 = input("Please enter in YYYY-MM-DD HH:MM:SS format ")
day2 = input("Please enter in YYYY-MM-DD HH:MM:SS format ")
print(diffFunction(day1, day2))