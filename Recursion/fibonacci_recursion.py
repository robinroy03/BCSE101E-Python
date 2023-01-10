# to find the nth fibonacci number using recursion (index starts from 0)

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)