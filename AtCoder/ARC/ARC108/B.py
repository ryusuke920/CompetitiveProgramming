n = int(input())
s = input()
ans = n
fox = []
word = "fox"
for i in range(n):
    if s[i] in word:
        fox.append(s[i])
        if len(fox) >= 3:
            if (fox[-3] == "f" and fox[-2] == "o" and fox[-1] == "x"):
                fox.pop()
                fox.pop()
                fox.pop()
                ans -= 3
    else:
        fox = []
print(ans)