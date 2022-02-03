N=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(N-1):
    if a[i]==a[i+1]:
        print("NO")
        break
else:
    print("YES")