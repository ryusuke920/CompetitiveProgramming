import sys
sys.setrecursionlimit(500_000)

x_next = [{}]
x_term = [False]
y_next = [{}]
y_sub = [0]
y_block = [False]
total_y = 0
covered_y = 0
Q = int(input())
for _ in range(Q):
    t, s = input().split()
    if t == "1":
        p = 0
        for i in s:
            if i not in x_next[p]:
                x_next[p][i] = len(x_next)
                x_next.append({})
                x_term.append(False)
                # print(i, x_next, x_term)
            p = x_next[p][i]
        x_term[p] = True

        p = 0
        path = [0]
        cover_ans = False
        for i in s:
            if y_block[p]:
                cover_ans = True
            if i not in y_next[p]:
                p = None
                break
            p = y_next[p][i]
            path.append(p)
        if p is not None and not cover_ans and not y_block[p]:
            c = y_sub[p]
            if c > 0:
                # print(c, covered_y, y_block)
                covered_y += c
                y_block[p] = True
                for a in path[:-1]:
                    y_sub[a] -= c
    if t == "2":
        total_y += 1
        p = 0
        tmp_x = False
        for i in s:
            if i not in x_next[p]:
                break
            p = x_next[p][i]
            if x_term[p]:
                tmp_x = True
                break
        p = 0
        cover_ans = y_block[0]
        nodes = []
        for i in s:
            if cover_ans or y_block[p]:
                cover_ans = True
            if i not in y_next[p]:
                y_next[p][i] = len(y_next)
                y_next.append({})
                y_sub.append(0)
                y_block.append(False)
                # print("koko")
            p = y_next[p][i]
            nodes.append(p)
            # print(nodes)
        if cover_ans:
            covered_y += 1
        elif tmp_x:
            covered_y += 1
        else:
            for u in nodes:
                y_sub[u] += 1

    print(total_y - covered_y)
