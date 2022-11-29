#A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.





s = input()
alpha_set = set(char for char in s.lower() if char.isalpha())
print("pangram" if len(alpha_set) == 26 else "not pangram")