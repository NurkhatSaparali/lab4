import datetime
today=datetime.datetime.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print(today)
print(yesterday)
print(tomorrow)
