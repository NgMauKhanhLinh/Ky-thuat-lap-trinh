def CheckDoiXung(s):
    flag=True
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            flag=False
            break
    return flag

def main():
    print("Nhập 1 chuỗi: ", end='')
    s = input()
    if (CheckDoiXung(s)):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")
while True:
    main()
    print("Tiếp tục không?(c/k): ",end='')
    x=input()
    if x=="k":
        print("Cảm ơn!")
        break
