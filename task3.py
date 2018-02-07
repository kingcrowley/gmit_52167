n = 17
# David Crowley

# loop to calculate Collatz conjecture
# https://en.wikipedia.org/wiki/Collatz_conjecture
# if the number is even then half it - otherwise multiply the number by 3 and add 1
print (n)
while not(n==1):
 
 if n % 2 == 0:
     n = n * 0.5
 else:
    n = (n * 3) + 1
 print (n)

 # output if n = 17 = 17,52,26,13,40,20,10,5,16,8,4,2,1
 


