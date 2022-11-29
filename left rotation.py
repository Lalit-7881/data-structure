#A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. Given an integer, , rotate the array that many steps left and return the result.


n, d = map(int, input().split())
arr = [int(x) for x in input().split()]

for i in range(d):
    arr.append(arr[i])
    
for x in arr[d:]:
    print(x, end=' ')