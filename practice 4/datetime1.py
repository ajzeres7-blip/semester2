import datetime
x=datetime.datetime(2026,3,14,14,30,0)
y=datetime.datetime(2026,3,13,8,12,0)
diff=x-y
print(diff.total_seconds()*60)
print(diff)
print(diff.days)
print(diff.seconds)
print(x.year)
print(x.month)
print(x.strftime("%d %A %I:%M%p %Y"))
print(x.strftime("%Y-%B-%d %H:%M:%S"))
#6544800.0
#1 day, 6:18:00
#1
#22680
#2026
#3
#14 Saturday 02:30PM 2026
#2026-March-14 14:30:00