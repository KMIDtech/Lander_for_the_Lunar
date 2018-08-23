def fibonnaci(a, b):
    print(a)
    print(b)
    for x in range(0,14):
        c = a + b
        a = b
        b = c
        print(c)

fibonnaci(0, 1)

def reverse_fib(c,b):
    print(c)
    print(b)
    for x in range(0, 14):
        a = c - b
        c = b
        b = a
        print(a)
reverse_fib(610, 377)