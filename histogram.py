""" find the lasrgest area in histogram"""
a=[2, 1, 5, 6, 2, 3]
stack=[]
max_area=float('-inf')
for i in range(len(a)):
    if not stack:
        stack.append(i)
    else:
        if a[i]> a[stack[-1]]:
            stack.append(i)
        else:
            while stack and  a[i] < a[stack[-1]]:
                element=a[stack.pop()]
                nsi=i
                psi=stack[-1] if stack else -1
                area=element*(nsi-psi-1)
                max_area=max(max_area,area)
                print(max_area)
            stack.append(i)

while stack:
    element=stack.pop()
    nsi=len(a)
    psi=stack[-1] if stack else -1
    area=element*(nsi-psi-1)
    max_area=max(max_area,area)
    print(max_area)

print(max_area)

