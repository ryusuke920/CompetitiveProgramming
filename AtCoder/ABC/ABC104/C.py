from itertools import product

d, g = map(int,input().split())
p, c = [0] * d, [0] * d
for i in range(d):
    p[i], c[i] = map(int,input().split())

ans = 10 ** 18
for i in product([0, 1], repeat=d):
    score = 0 # 得点
    problem = 0 # 解いた問題数
    need = [] # 貪欲にとっていくやつ
    for j in range(d):
        if i[j] == 1:
            score += (j + 1) * 100 * p[j] + c[j]
            problem += p[j]
        else:
            for _ in range(p[j]):
                need.append(100 * (j + 1))
    
    if score >= g:
        ans = min(ans, problem)
    else:
        need.sort(reverse=True)
        t = 0
        l = len(need)
        while True:
            if score >= g:
                ans = min(ans, problem)
                break
            if t >= l - 1: break
            score += need[t]
            problem += 1
            t += 1

print(ans)