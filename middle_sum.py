n=239017
n_str=str(n)

length=len(str(n))
mid=int((length/2))
first_total=0
second_total=0
for i in range(len(n_str)):
    if i < mid:
       first_total=first_total+int(n_str[i]) 
    else:
        second_total=second_total+int(n_str[i]) 

print(first_total)
print(second_total)


