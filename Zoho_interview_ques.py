version1="2.4.23"
version2="2.04.25"
c=[]
d=[]
digit=""
for i in version1:
    if i != ".":
        digit=digit+i
    else:
        c.append(int(digit))
        digit=""
c.append(int(digit))
digit=""
for i in version2:
    if i != ".":
        digit=digit+i
    else:
        d.append(int(digit))
        digit=""
d.append(int(digit))
count=0
for i in range(len(c)):
    if c[i]<d[i]:
        print("Output :")
        print("upgrade")
        break
    elif c[i]>d[i]:
        print("downgrade")
        break
    else:
        count=count+1
if count==len(c):
    print("Equal")


