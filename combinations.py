# Task 15

#You are given a string S.
#Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

from itertools import combinations

n = input().split()
S = n[0]
k = int(n[1])
for i in range(1,k+1):
    for j in combinations(sorted(S),i):
        print("".join(j))
