import datetime

start = datetime.datetime.now()

test = "12:49:00.123"
end = datetime.datetime.strptime(test, '%H:%M:%S.%f')

s = (start - end).seconds
ms = (start - end).seconds * 1000

print(int(ms))