n = int(input())
h = n//3600
m = (n - h*3600)//60
s = (n - h*3600 - m*60)
print(h,":",m,":",s, sep = "")