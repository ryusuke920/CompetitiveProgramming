n = int(input())
a = list(map(int, input().split()))
ans = []
for i in a:
    while i%2 == 0:
        i /= 2
    ans.append(i)
print(len(set(ans)))