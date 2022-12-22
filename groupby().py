#task 17

#In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools .


from itertools import *

S = input()
for i,j in groupby(map(int,list(S))):
    print(tuple([len(list(j)), i]) ,end = " ")
