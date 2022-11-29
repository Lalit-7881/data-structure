#Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
#Declare an integer, , and initialize it to .

#There are  types of queries, given as an array of strings for you to parse:







a = input().split(' ')
N, Q = [int(e) for e  in a]
arrays = [[] for _ in range(N)]
lastans = 0

def insert(x, y):
    global lastans
    arrays[(x ^ lastans) % N].append(y)
def printnum(x, y):
    global lastans
    inst = arrays[(x ^ lastans) % N]
    lastans = inst[y % len(inst)]
    print(lastans)
    
    
for i in range(Q):
    line = [int(e) for e in input().split(' ')]
    insert(line[1], line[2]) if line[0] == 1 else printnum(line[1], line[2])
