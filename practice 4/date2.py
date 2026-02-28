import datetime
x=datetime.datetime.now()
y=datetime.timedelta(days=1)
yesterday=x-y
tommorrow=x+y
print(yesterday.strftime("%Y-%B-%d"))
print(x.strftime("%Y-%B-%d"))
print(tommorrow.strftime("%Y-%B-%d"))