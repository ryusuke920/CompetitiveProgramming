s = list(input())
k = int(input())
one = two = 0
ch1 = set(s)
ch2 = s
ch3 = s*2
for i in range(len(s)-1):
    if ch2[i] == ch2[i+1]:
        ch2[i+1] = "1"
        one += 1

for i in range(len(ch3)-1):
    if ch3[i] == ch3[i+1]:
        ch3[i+1] = "1"
        two += 1

d = two - one

an = one + (k-1)*d

if len(ch1) == 1:
    print(len(s)*k//2)
else:
    if s[0] == s[-1]:
        print(an)
    else:
        print(one*k)