n = int(input())
h = n//3600
s = n%60
m = (n-(3600*h+s))//60
print(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2))