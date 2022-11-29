#We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber that a subsequence maintains the order of characters selected from a sequence.



#!/bin/python3

import sys
import re

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    
    pattern = ".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*"
    m = re.search(pattern, s)
    if m is not None:
        print("YES")
    else:
        print("NO")