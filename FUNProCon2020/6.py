ans = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
s = input()
s = s[::-1]
if s in ans:
    for i in range(36):
        if ans[i] == s:
            exit(print(i + 1))
num = 0
for i in range(len(s)):
    for j in range(36):
        if s[i] == ans[j]:
            if i == 0:
                num += j + 1
            else:
                num += (j + 1)*(36 ** i)
print(num)