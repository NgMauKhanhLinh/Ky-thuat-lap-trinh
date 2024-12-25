def move (n,A,B,C):
    if n==1:
        print(f"move {A}=>{C}")
    else:
        move(n-1,A,C,B)
        print(f"move {A}=>{C}")
        move(n-1,B,C,A)