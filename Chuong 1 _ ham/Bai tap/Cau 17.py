def He10sangHe16(n):
    if n>0:
        sd=n%16
        n=n//16
        He10sangHe16(n)
        if sd==10:
            sd="A"
        if sd==11:
            sd="B"
        if sd==12:
            sd="C"
        if sd==13:
            sd="D"
        if sd==14:
            sd="E"
        elif sd==15:
            sd="F"
        print (sd,end='')

n=317547
print(f"Hệ thập phân sang thập lục phân của {n} là:", end="")
He10sangHe16(n)