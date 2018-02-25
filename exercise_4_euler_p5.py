# David Crowley g00364706
# Problem
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Smallest positive number that is evenly divisible is the Greatest Common Divisor (gcd)
from fractions import gcd
a = [1, 2, 3, 4, 5, 6, 7 , 8, 9 , 10,11, 12, 13, 14, 16, 17, 18, 19, 20]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
 # print(gcd(lcm, i))
 # finding the lcm of the current lcm and i
 # current lcm * i / greatest common divisor of the lcm and i 
  lcm = lcm*i/gcd(lcm, i)
 # print("Current lcm: "+ str(lcm))
print("Overall :"+ str(lcm))

# answer is 232792560