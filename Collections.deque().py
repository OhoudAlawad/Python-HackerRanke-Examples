# Task 22

# Perform append, pop, popleft and appendleft methods on an empty deque .

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

storage = deque()
N = int(input())

for i in range(N):
    val = input().split()
    if(val[0] == 'append'):
        storage.append(val[1])
    elif(val[0] == 'popleft'):
        storage.popleft()
    elif(val[0] == 'appendleft'):
        storage.appendleft(val[1])
    elif(val[0] == 'pop'):
        storage.pop()

print(' '.join(storage))
