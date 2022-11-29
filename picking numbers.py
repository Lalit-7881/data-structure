#Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .


#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
count=0
for i in height:
    if i>k:
        count+=i-k
        k=i
print(count)
