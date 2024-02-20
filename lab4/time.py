import datetime
# from datetime import datetime, date, time

# def backToPast(n):
#     return datetime.date.today() - datetime.timedelta(n)

# value = int(input("enter how far to go back"))
# print(backToPast(value))


# def threeDays():
#     yesterday = datetime.date.today() - datetime.timedelta(1)
#     today = datetime.date.today()
#     tomorrow = datetime.date.today() + datetime.timedelta(1)
#     return yesterday, today, tomorrow

# print(threeDays())


# def dropMilliseconds():
#     rightNow = datetime.datetime.now()
#     formatted = rightNow.strftime("%m/%d/%Y, %H:%M:%S")
#     return formatted

# print(dropMilliseconds())


def difference(str1, str2):
    day1_object = datetime.datetime.strptime(str1, '%m/%d/%y %H:%M:%S')
    day2_object = datetime.datetime.strptime(str2, '%m/%d/%y %H:%M:%S')
    diff = day1_object - day2_object
    return diff.second()


day1 = input("Please enter in mm/dd/yyyy HOURS:MINUTES:SECONDS format ")

day2 = input("Please enter in mm/dd/yyyy HOURS:MINUTES:SECONDS format ")

print(difference(day1, day2))