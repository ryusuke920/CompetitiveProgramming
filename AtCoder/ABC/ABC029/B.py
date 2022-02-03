s = [str(input()) for i in range(12)]
count = 0
for i in range(12):
    if "r" in s[i]:
        count += 1
print(count)