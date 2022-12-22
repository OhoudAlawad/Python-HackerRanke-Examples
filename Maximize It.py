#Task 19

#Maximize It

# You are given a function f(x) = x^2. You are also given k lists. The ith list consists of Ni elements. You have to pick one element from each list so that the value from the equation below is maximized:

#S = ( f(X1) + f(X2) + ......+ f(Xk))%M

#....

# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import *

K, M = map(int, input().split())
N = []

for _ in range(K):
    N.append(map(int, input().split()[1:]))
    MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)

print (MAX)
