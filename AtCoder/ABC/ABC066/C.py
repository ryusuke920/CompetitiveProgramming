n = int(input())
a = list(map(int,input().split()))
print(*(a[::-2]+a[n%2::2]))