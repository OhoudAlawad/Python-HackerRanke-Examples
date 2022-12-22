# Task 13

# You are given a string S.
#Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

from itertools import permutations

s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')
