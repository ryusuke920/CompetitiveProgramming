cnt = [0] * 10
correct = 0

for _ in range(int(input())):
    a, b, c, d, judge = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    
    if judge == 'YES':
        correct += 1
        cnt[a] += 1
        cnt[b] += 1
        cnt[c] += 1
        cnt[d] += 1
    elif judge == 'NO':
        cnt[a] -= 1
        cnt[b] -= 1
        cnt[c] -= 1
        cnt[d] -= 1    

print(cnt.index(correct))