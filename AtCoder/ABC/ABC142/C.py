n = int(input())
a = list(map(int,input().split()))
s = {}
for i in range(n):
    #print("i = ",i,"の時a[",i,"] = ",a[i],"で,s[",a[i],"] = ",i+1)
    s[a[i]] = i+1
for i in range(n):
    print(s[i+1])