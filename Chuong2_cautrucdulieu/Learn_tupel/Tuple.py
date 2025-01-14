def split_number(n):
    n1=n//100
    n2=n//10%10
    n3=n%10
    return (n1,n2,n3)

n1,n2,n3  =split_number(587)
print("n1=",n1)
print("n2=",n2)
print("n3=",n3)