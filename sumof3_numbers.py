a=[4,0,1,-2,3]
n=len(a)
res=[]
for i in range(n):
    first=0
    second=0
    mid=a[i]
    if i-1>=0:
        first=a[i-1]
    if i+1<n:
        second=a[i+1]
    summ=first+mid+second
    res.append(summ)

print(res)