from collections import deque

s = input()

q = deque()
stack = []
for i in s:
    if i == '(':
        continue