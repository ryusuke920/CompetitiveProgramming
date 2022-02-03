import datetime
y,m,d = map(int,input().split('/'))
D = datetime.datetime(y,m,d)
while D.year%D.month != 0 or D.year//D.month%D.day != 0:
    D += datetime.timedelta(days = 1)
print(D.strftime('%Y/%m/%d'))