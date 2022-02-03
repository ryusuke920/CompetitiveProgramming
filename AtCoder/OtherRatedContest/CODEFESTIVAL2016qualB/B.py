n, a, b = map(int,input().split())
s = input()
a_p = 0
b_p = 0
 
for i in s:
    if i == 'a' and a_p + b_p < a + b:
        print('Yes')
        a_p += 1
    elif i == 'b' and a_p + b_p < a + b and b_p < b:
        print('Yes')
        b_p += 1
    else:
        print('No')