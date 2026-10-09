#find the largest product of adjacent numbers
n=[8,-6,-2,-5,7,3]
max_prod=0
for i in range(len(n)):
    first=n[i]
    if i+1 <len(n):
        second=n[i+1]
        max_prod=max(max_prod,(first*second))

print(max_prod)