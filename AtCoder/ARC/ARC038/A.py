n = int(input())
a = list(map(int,input().split()))
a = sorted(a,reverse = True)
print(sum(a[0::2]))