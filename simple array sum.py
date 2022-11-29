#Given an array of integers, find the sum of its elements.

#For example, if the array , , so return .





n = int(input())
nums = list(map(int, input().split()))
sum = 0
for num in nums:
    sum += num
print(sum)