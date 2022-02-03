n = int(input())
ans1 = 2
ans2 = 1
ans3 = 3
for i in range(1,n):
    ans3 = ans1 + ans2
    ans1 = ans2 
    ans2 = ans3
if n == 1:
    print(1)
else:
    print(ans3)