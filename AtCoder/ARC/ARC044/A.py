n = int(input())
x = n
if n == 1:
    print("Not Prime")
    exit()
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        ans = 0
        while n != 0:
            ans += n%10
            n = n//10
        if x%10 != 5 and x%2 != 0 and ans%3 != 0:
            print("Prime")
            exit()
        else:
            print("Not Prime")
            exit()
else:
    print("Prime")