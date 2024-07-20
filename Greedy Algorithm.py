# Greedy Algorithm:

# There are 4 possible Constrains in this problem to only possible to solve using Greedy:
# 1. Subproblem
# 2. Greedy Choice
# 3. No Backtracking
# 4. Proof Of Correctness

amount=8
coins=[1,2,5]
# or coins=[1,5,10,20]

coins.sort(reverse=True)
count=0
for coin in coins:
    count+=amount//coin
    amount=amount%coin
print(count)



# In this case Cannot be Greedy algoritm is Appling for all test case
# because amount =8 but change give only amount=7.So achieve all the test case
# using also Backtracking .so greedy is not suitable in this case.

amount=8
coins=[2,5]

coins.sort(reverse=True)
count=0
for coin in coins:
    count+=amount//coin
    amount=amount%coin
if amount==0:
    print(count)
else:
    print("Cannot Make Change")
