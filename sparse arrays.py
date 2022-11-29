#There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.


from collections import Counter

def matchingStrings(strings, queries):
    c = Counter(strings)
    return (c[i] for i in queries)

n = int(input())
strings = [input() for _ in range(n)]
q = int(input())
queries = [input() for _ in range(q)]
print(*matchingStrings(strings, queries),sep="\n")