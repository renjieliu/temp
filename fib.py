def fib(n):
    if n <= 0:

        return -1
    elif n < 3:
        return 1
    else:
        a = b = 1 
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        return c 


print(fib(100))
print(fib(-1))

