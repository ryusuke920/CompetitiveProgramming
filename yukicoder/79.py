n = int(input())
l = list(map(int, input().split()))

cnt = [0] * 10 ** 5
for i in l:
    cnt[i - 1] += 1

ma = max(cnt)
for i in reversed(range(10 ** 5)):
    if cnt[i] == ma:
        exit(print(i + 1))