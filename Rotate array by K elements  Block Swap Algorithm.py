N = 5
array = [1,2,3,4,5]
K=2
arr=[0]*N
for i in range(N):
    arr[(K+i)%N]=array[i]
print(arr)
