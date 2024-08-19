num=[1, 5, 3, 5, 6, 1]
d={}
minnn=len(num)
repeating=False
for i in range(len(num)):
    minn=0
    if num[i] in d:
        repeating=True
        minn=i-d[num[i]]
        d[num[i]] = i
        minnn=min(minn,minnn)
    else:
        d[num[i]]=i
if repeating:
    print(minnn)
else:
    print(-1)



