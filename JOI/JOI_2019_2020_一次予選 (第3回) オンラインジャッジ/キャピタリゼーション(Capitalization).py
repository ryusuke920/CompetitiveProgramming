n = int(input())
s = list(input())
i = 0
while i < n - 2:
    if s[i] == "j" and s[i+1] == "o" and s[i+2] == "i":
        s[i] = "J"
        s[i+1] = "O"
        s[i+2] = "I"
        i += 2
    i += 1
print(*s, sep = "")