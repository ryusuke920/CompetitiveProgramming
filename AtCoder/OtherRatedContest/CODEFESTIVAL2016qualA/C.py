s = list(input())
k = int(input())
for i in range(len(s)):
    num = (123 - ord(s[i]))
    if s[i] == 'a': continue
    if num > k: continue
    s[i] = 'a'
    k -= num
s[-1] = chr(97 + (ord(s[-1]) - 97 + k) % 26)
print(*s, sep = '')