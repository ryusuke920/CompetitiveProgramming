from collections import deque
n = int(input())
s = input()

q = deque()
l = 0
for i, j  in enumerate(s):
    if j == "L":
        q.appendleft(i + 1)
        l += 1
    elif j == "R":
        q.append(i + 1)
        l += 1
    elif j == "A":
        if l <= 0:
            print("ERROR")
        else:
            x = q.popleft()
            print(x)
            l -= 1
    elif j == "B":
        if l <= 1:
            print("ERROR")
        else:
            x = q.popleft()
            y = q.popleft()
            print(y)
            q.appendleft(x)
            l -= 1
    elif j == "C":
        if l <= 2:
            print("ERROR")
        else:
            x = q.popleft()
            y = q.popleft()
            z = q.popleft()
            print(z)
            q.appendleft(y)
            q.appendleft(x)
            l -= 1
    elif j == "D":
        if l <= 0:
            print("ERROR")
        else:
            x = q.pop()
            print(x)
            l -= 1
    elif j == "E":
        if l <= 1:
            print("ERROR")
        else:
            x = q.pop()
            y = q.pop()
            print(y)
            q.append(x)
            l -= 1
    elif j == "F":
        if l <= 2:
            print("ERROR")
        else:
            x = q.pop()
            y = q.pop()
            z = q.pop()
            print(z)
            q.append(y)
            q.append(x)
            l -= 1