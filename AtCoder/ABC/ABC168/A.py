N=int(input())
if (N%10==0 or N%10==1 or N%10==6 or N%10==8):
    print("pon")
elif (N%10==3):
    print("bon")
else:
    print("hon")