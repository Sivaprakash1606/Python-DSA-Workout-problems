def diven(input1, k):
    l = list(map(int, str(input1)))
    i = 0
    max1 = []
    empty = []
    while k <= len(l):
        sub = l[i:k]
        ub = max(l[i:k])
        max1.append(ub)
        empty.append(sub)
        i = i + 1
        k = k + 1
    return int(''.join(map(str, max1))), empty

input1 = 247163
k = 3
given = diven(input1, k)
print(given[0])
print(given[1])


class Solution:
    def pivotInteger(self, n) :
        num = 0
        a = n
        for i in range(n + 1):
            num = num + i
        for i in range(n):
            current = a
            if num == n:
                return current
            else:
                num = num - current
                a = a - 1
                n = n + a
        return -1

n=8
print(Solution().pivotInteger(n))

