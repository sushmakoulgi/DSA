inputarray=["aa","chd","ewr","er","r"]
max_length=float('-inf')
from collections import defaultdict

result=defaultdict(list)
for item in inputarray:
    length=len(item)
    result[length].append(item)
    max_length=max(max_length,length)

print(result[max_length])

