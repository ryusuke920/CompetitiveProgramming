n = int(input())
a = list(map(int,input().split()))
if len(set(a)) % 2 == 0:
    print(len(set(a)) - 1)
else:
    print(len(set(a)))