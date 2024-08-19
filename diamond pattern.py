num=5
for i in range(0,num):
    l=num-(num-i//2)
    r=l+i
    for j in range(0,num):
        if j>=l and j<=r:
            print("*",end=" ")
        else:
            print(end="  ")
    print(" ")


