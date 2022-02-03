from collections import deque
x = input()
stack = deque(x[0])
for i in range(1,len(x)):
    if x[i] == "S":
        stack.appendleft(x[i])
    else: #x[i] == "T"
        if len(stack) == 0:
            stack.append(x[i])
        elif stack[0] == "T":
            stack.appendleft(x[i])
        else: #stack[0] == "S"
            stack.popleft()
print(len(stack))