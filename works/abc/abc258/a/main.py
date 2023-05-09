import datetime

k = int(input())
d = datetime.datetime(2021, 5, 1, 21, 0, 0)
d = d+ datetime.timedelta(minutes=k)

print(d.strftime("%H:%M"))