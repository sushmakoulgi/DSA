arr=[-1,2,3,3,4,5,-1]

window_size=4
i=0
max_sum=float('-inf')
for i in range(len(arr)):
    j=i+3
    if j<=len(arr):
        window=arr[i:j]
        print(window)
        total=sum(window)
        max_sum=max(max_sum,total)
print(max_sum)

    
