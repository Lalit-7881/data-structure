#In this challenge, you will determine whether a string is funny or not. To determine whether a string is funny, create a copy of the string in reverse e.g. . Iterating through each string, compare the absolute difference in the ascii values of the characters at positions 0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both strings, they are funny.


import sys

strings = []
for line in sys.stdin:
    strings.append(line.strip())

for i in strings[1:]:
    S = i
    R = i[::-1]
    funny = True
    for j in range(1, len(i)):
        if abs(ord(S[j]) - ord(S[j-1])) != abs(ord(R[j]) - ord(R[j-1])):
            funny = False
            break
            
    if funny:
        print("Funny")
    else:
        print("Not Funny")