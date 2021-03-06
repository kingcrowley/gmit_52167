# David Crowley g00364706
# Problem
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Smallest positive number that is evenly divisible is the Greatest Common Divisor (gcd)

# Code from link below
# https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python/42472824


import time
from fractions import gcd
a = [1, 2, 3, 4, 5, 6, 7 , 8, 9 , 10,11, 12, 13, 14, 16, 17, 18, 19, 20]   #will work for an int array of any length
lcm = a[0]
# get current time (unix time)
start = time.time()
for i in a[1:]:

 # print(gcd(lcm, i))
 # finding the lcm of the current lcm and i by dividing by the gcd
 # current lcm * i / greatest common divisor of the lcm and i 

 # if we know the greatest common divisor (GCD) of integers a and b, 
 # we can calculate the LCM using the following formula. LCM(a,b) = (a*b)/GCD(a,b)
 # found this info comes from at https://www.idomaths.com/hcflcm.php 
  lcm = lcm*i/gcd(lcm, i)
# used for debugging to comapre start time to current time
#print(time.time())
# timetaken = current time - the start time
elapsed = (time.time() - start)
print ("LCM = %s returned in %f seconds."% (lcm,elapsed))
# answer is 232792560 - time take is normally too small for this simple calculation to see
