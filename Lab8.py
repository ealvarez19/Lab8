"""
Emmanuel Alvarez 80567137
Instructor: Olac Fuentes
Last day modified: 05-13-2019
The purpose of this code is to compare two different equations and return is they 
are equal or not using randomization algorithm. Also, given a Set, return if it has two 
different subsets that add up the same integer. 
"""


import random
import numpy as np
from math import *
from mpmath import mp 

def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        z = random.uniform(-pi,pi) #creates a random number between -pi and pi
        f1 = f1.replace("x",str(z)) #replace the x character of the string by the random value created
        f2 = f2.replace("x",str(z))
        y1 = eval(f1) # evaluates the equation
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance: #compares both equations wheater they are equal 
            return False
    return True


def subsetsum(S,last,goal,subset2):    
    if goal ==0:        
        subset2.append(S[last]) # Appends S[last] if goal is 0 to subset2 
        return True, [],subset2
    if goal<0 or last<0: # Appends S[last] to subset2
        subset2.append(S[last+1])
        return False, [], subset2
    res, subset,subset2 = subsetsum(S,last-1,goal-S[last],subset2) # Take S[last]
    if res:
        subset.append(S[last])       
        return True, subset,subset2
    else:
        return subsetsum(S,last-1,goal,subset2) # Don't take S[last]


equations = ['sin(x)','cos(x)','tan(x)','mp.sec(x)','-sin(x)','-cos(x)','-tan(x)','sin(-x)','cos(-x)','tan(-x)','sin(x)/cos(x)','2*sin(x/2)*cos(x/2)','sin(x)*sin(x)','1 - cos(x) * cos(x)','(1 - cos(2*x)/2)','1 / cos(x)']
for i in range(len(equations)):
    for j in range(i+1,len(equations)):
        print(equations[i]," and ",equations[j]," are equal? ",equal(equations[i],equations[j]))
        
print("----------------------------------------------------------------------------------------------") 
S = [2,4,5,9,12]
total = 0
for t in S:
    total+=t
print("Set: ", S)
print("Subsets that add up the same integer: ")
subset2 = []
a,b,c = subsetsum(S,len(S)-1,total/2,subset2)
print(a,b,c)
