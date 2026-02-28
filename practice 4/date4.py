import datetime
dt1=datetime.datetime(2026,12,31,14,0,0)
dt2=datetime.datetime(2026,2,28,10,0,42)
diff=dt1-dt2
print(diff.total_seconds())