n = int(input())
s = input()
for i in range(n - 1):
    if (s[i] == "a" and s[i + 1] == "b") or (s[i] == "b" and s[i + 1] == "a"):
        exit(print("Yes"))

print("No")