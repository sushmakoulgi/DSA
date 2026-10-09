a=[2, 1, 5, 1, 3, 2]
k=3
right=0
left=0
max_sum=0

for i in range(len(a)):
    right=i+k
    if right <= len(a):
        window=a[left:right]
        print(window)
        total=sum(window)
        max_sum=max(max_sum,total)
        left=left+1

print(max_sum)