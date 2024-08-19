string="     Merfantz   Tech    Pvt    Ltd        Welcome     "
s=string.split()
spaces=[]
count=0
for i in string:
    if i == " ":
        count+=1
    else:
        if count!=0:
            spaces.append(count)
            count=0
spaces.append(count)
n=len(spaces)-2
print(spaces)
for i in s:
    print(i,end=" ")
print()
print(f"First space count: {spaces[0]}")
print(f"Last space count: {spaces[-1]}")
print(f"Middle space count: {sum(spaces[1:-1])-n}")

