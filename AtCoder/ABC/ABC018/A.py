A = int(input())
B = int(input())
C = int(input())
if A>B and A>C and B>C:
    print(1)
    print(2)
    print(3)
elif A>B and A>C and C>B:
    print(1)
    print(3)
    print(2)
elif B>A and B>C and A>C:
    print(2)
    print(1)
    print(3)
elif B>A and B>C and C>A:
    print(3)
    print(1)
    print(2)
elif C>A and C>B and A>B:
    print(2)
    print(3)
    print(1)
else :
    print(3)
    print(2)
    print(1)