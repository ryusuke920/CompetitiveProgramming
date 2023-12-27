s = input()
q = ["-", "-"]
for i in s:
    q.append(i)
    if "".join(q[-3:]) == "ABC":
        q.pop()
        q.pop()
        q.pop()

print(*q[2:], sep="")

