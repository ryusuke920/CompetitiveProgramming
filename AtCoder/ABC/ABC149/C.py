N=int(input())
while True:
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            N+=1
            break
    else:
        break
print(N)