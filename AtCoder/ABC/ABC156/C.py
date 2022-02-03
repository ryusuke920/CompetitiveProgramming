n = int(input())
x = list(map(int,input().split()))
count1 = 0
count2 = 0
x.sort ()
ans1 = sum(x)//n
ans2 = ans1+1
for i in range(n):
    count1 += (x[i]-ans1)**2
    count2 += (x[i]-ans2)**2
print(min(count1,count2))