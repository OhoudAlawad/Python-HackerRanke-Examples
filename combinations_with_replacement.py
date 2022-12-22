#Task 16
#You are given a string S.
#Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

from itertools import combinations_with_replacement

x = input().split();
S = sorted(x[0]);
K = int(x[1]);

for i in combinations_with_replacement(S,K):
    print(''.join(i));
