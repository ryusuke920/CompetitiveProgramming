n = int(input())
a = list(map(int,input().split()))
num = [[a[i],i+1] for i in range(n)]
num.sort(key = lambda x: x[0], reverse = True)
for i in range(n):
    print(num[i][1])