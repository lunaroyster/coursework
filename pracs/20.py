def cube(n): return n**3

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b
    return

def powersOfTwo(n):
    for i in range(n):
        yield 2**i
    return