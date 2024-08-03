x="program"

for i in range(len(x)):
    j=len(x)-1-i
    for k in range(len(x)):
        if (k==i or k==j):
            print(x[k],end="")
        else:
            print(end=" ")
    print(" ")






