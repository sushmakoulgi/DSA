#max consecutive ones
a=[1,1,1,0,0,0,1,1,1,1,0]
l=[]
max_len=0
k=2

def consecutive():
    k=2
    res=[]
    group=[]
    for i in range(len(a)):
          #start over
        res=[]
        k=2
        for j in range(len(a)):
            if j>=i:
                if a[j]==1:
                    res.append(a[j])
                elif a[j]==0:
                    if k >0:
                        res.append(a[j])
                        k=k-1
                    else:
                        print(res)
                        group.append(res)
                        break

    return res

print(consecutive())


