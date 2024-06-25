string="     Merfantz   Tech    Pvt    Ltd        Welcome     "
spaces=[]
count=0
for i in range(len(string)):
    if string[i] == " ":
        count+=1
    else:
        if count!=0:
            spaces.append(count)
            count=0
spaces.append(count)
n=len(spaces)-2
print(spaces)
print(f"First space count: {spaces[0]}")
print(f"Last space count: {spaces[-1]}")
print(f"Middle space count: {sum(spaces[1:-1])-n}")


