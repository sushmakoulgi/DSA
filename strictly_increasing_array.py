#strictly increasing array by just removing one item
a=[1,5,3,4]
def solution(a):
    removed=False
    valid=False
    for i in range(len(a)-1):
        if i+1 <len(a) and a[i+1] > a[i]:
            print(f"comparing {a[i]} and {a[i+1]}")
            print("its incresing")
            pass
        else:
            if not removed:
                print("removing success ",a[i])
                removed=True
            else:
                print("removing ",a[i])
                return False
              
    return True


print(solution(a))
