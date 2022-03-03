# Fibonacci numbers module
	
def fib(n):
    a, b, c = 1, 2, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
        if c == 1 :
            print(a)
            c = c+1
    print()
fib(1000)