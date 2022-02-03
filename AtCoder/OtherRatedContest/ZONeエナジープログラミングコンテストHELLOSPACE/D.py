from collections import deque
s = input()

q = deque([])
turn = 0

for i in s:
    if i == "R":
        turn ^= 1
    elif turn: # 通常時
        # 先頭と今入ってきたものが同じであればpopleft()
        if q and q[0] == i:
            q.popleft()
        else:
            q.appendleft(i)
    else: # 反転時
        # 末尾と今入ってきたものが一致してればpop()
        if q and q[-1] == i:
            q.pop()
        else:
            q.append(i)

if turn == 1:
    print("".join(q)[::-1])
else:
    print("".join(q))