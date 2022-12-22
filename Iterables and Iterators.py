#Task 18

#  You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
#Find the probability that at least one of the K indices selected will contain the letter: 'a'.


from itertools import combinations

N = int(input())
char = input().split()
K = int(input())

count = 0;
total = 0;

for i in combinations(char,K):
    count += 'a' in i
    total += 1
    
print(count/total)

