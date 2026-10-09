"""
# F(0) = 0
# F(1) = 1
# F(n) = F(n − 1) + F(n − 2), for n > 1
# """


def fib(n):
    if n==0 or n==1:
        return n
    return  (fib(n-1) +fib(n-2))


print(fib(6))
