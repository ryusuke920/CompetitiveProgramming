h, w, c, q = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(q)][::-1]

done_w = set()
done_h = set()
ans = [0] * c
for i in range(q):
    t, n, color = a[i]
    if t == 1 and n not in done_w:
        ans[color - 1] += w - len(done_h)
        done_w.add(n)
    elif t == 2 and n not in done_h:
        ans[color - 1] += h - len(done_w)
        done_h.add(n)

print(*ans)