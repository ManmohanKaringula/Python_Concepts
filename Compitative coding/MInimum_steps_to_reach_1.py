# This is problem in which the given number can be reduced to 1 using the prescribed rules with minimum number of steps
# Ex: 10 =>>(10-1 => 9, 9/3 => 3, 3/3 => 1) therefore the minimum step required is 3.
# RULES:
# 1. Decrement by 1.
# 2. Divide by 3.
# 3. Divide by 2.

def minSteps(target):
    x,y,z= target-1, target/2, target/3
    

