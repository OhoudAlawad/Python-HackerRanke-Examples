#Task 7
# Find Angle MBC in Python

# importing math
import math

# taking input from user
AB,BC=int(input()),int(input())

# calculating distance
M=math.hypot(AB,BC)      

# calculating the angle
ang=round(math.degrees(math.acos(BC/M))) 

# the 176 represents the degree symbol
degree=chr(176)                          
print(ang,degree, sep='')
