#Task 5
#The included code stub will read an integer, , from STDIN.

#Without using any string methods, try to print the following:
  #  123...n

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end="")
