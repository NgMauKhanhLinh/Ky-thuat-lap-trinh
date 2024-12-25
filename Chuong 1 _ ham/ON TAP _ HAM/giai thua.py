def giaithua (n):
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    return gt
gt_5=giaithua(5)
print("5!=",gt_5)