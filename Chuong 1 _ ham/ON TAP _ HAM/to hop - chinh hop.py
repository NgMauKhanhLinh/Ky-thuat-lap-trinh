def giaithua (n):
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    return gt

#CHINHHOP
def chinhhop (n,k):
    return giaithua(n)/giaithua(n-k)

#TO HOP
def tohop (n,k):
    return giaithua(n)/(giaithua(k)*giaithua(n-k))

print("5!=",gt_5)
print("A(5,3)=",chinhhop(5,3))