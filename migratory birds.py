#Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.


#!/bin/python3

import sys
from collections import Counter
import operator

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
mydict = dict(Counter(types))
maximum = max(mydict, key=mydict.get)  
print(maximum)