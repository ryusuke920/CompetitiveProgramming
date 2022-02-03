from collections import deque
n = int(input())
s = input()
a = deque()
num = 0

for i in range(n):
    if s[i] == 'L':
        a.appendleft(i + 1)
        num += 1
    elif s[i] == 'R':
        a.append(i + 1)
        num += 1
    elif s[i] == 'A':
        if num <= 0:
            print('ERROR')
        else:
            print(a.popleft())
            num -= 1
    elif s[i] == 'B':
        if num <= 1:
            print('ERROR')
        else:
            cnt = []
            for j in range(2):
                cnt.append(a.popleft())
            print(cnt[1])
            a.appendleft(cnt[0])
            num -= 1
    elif s[i] == 'C':
        if num <= 2:
            print('ERROR')
        else:
            cnt = []
            for j in range(3):
                cnt.append(a.popleft())
            print(cnt[2])
            for j in range(2):
                a.appendleft(cnt[1 - j])
            num -= 1
    elif s[i] == 'D':
        if num <= 0:
            print('ERROR')
        else:
            print(a.pop())
            num -= 1
    elif s[i] == 'E':
        if num <= 1:
            print('ERROR')
        else:
            cnt = []
            for j in range(2):
                cnt.append(a.pop())
            print(cnt[1])
            a.append(cnt[0])
            num -= 1
    elif s[i] == 'F':
        if num <= 2:
            print('ERROR')
        else:
            cnt = []
            for j in range(3):
                cnt.append(a.pop())
            print(cnt[2])
            for j in range(2):
                a.append(cnt[1 - j])
            num -= 1