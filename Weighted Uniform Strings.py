#A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are  to  from  to  as shown below:


s = input().strip()
cost = set()
prev = ''
count = 0
for i in s:
    if i != prev:
        prev = i
        count = 0
    count += 1
    cost.add(count * (ord(i) - ord('a') + 1))
for _ in range(int(input())):
    print("Yes" if int(input()) in cost else "No")